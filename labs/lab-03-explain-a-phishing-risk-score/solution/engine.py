from __future__ import annotations
import csv, json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
DATA=BASE/'data'/'input.csv'; EVIDENCE=BASE/'evidence'; EVIDENCE.mkdir(exist_ok=True)
OUTPUTS={
    1:['risk_register.csv','risk_summary.json'],2:['anomalies.csv','threshold-decision.md'],
    3:['phishing_triage.csv'],4:['prioritised_vulnerabilities.csv','sla-rationale.md'],
    5:['use_case_scorecard.csv','pilot-charter.md'],6:['threat_model.json','control_backlog.csv'],
    7:['programme_charter.md','RACI.csv'],8:['soc_architecture.json','ADR-001.md'],
    9:['retrieval_results.json','cited-analyst-brief.md'],10:['playbook.json','dry_run_report.json'],
    11:['action_plan.csv','roadmap.md'],12:['monitoring_report.json','advisory_report.md']}
def load():
    with DATA.open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def write_output(name,result):
    path=EVIDENCE/name
    if path.suffix=='.json':
        path.write_text(json.dumps(result,indent=2,default=str),encoding='utf-8')
    elif path.suffix=='.csv':
        records=result if isinstance(result,list) else [{'metric':k,'value':json.dumps(v,default=str)} for k,v in result.items()]
        if not records: records=[{'status':'no eligible records'}]
        fields=[]
        for row in records:
            for key in row:
                if key not in fields: fields.append(key)
        with path.open('w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore',lineterminator='\n'); writer.writeheader(); writer.writerows(records)
    elif path.suffix=='.md':
        title=path.stem.replace('-',' ').replace('_',' ').title()
        path.write_text(f'# {title}\n\n## Evidence-backed result\n\n```json\n{json.dumps(result,indent=2,default=str)}\n```\n\n## Decision boundary\n\nHuman review is required before production use or high-impact action.\n',encoding='utf-8')
    else: raise ValueError(f'unsupported output: {path}')
def run(lab_num):
    rows=load(); result=[]
    if lab_num==1:
        for r in rows:
            score=round(float(r['threat_likelihood'])*(float(r['criticality'])*5)*(1-float(r['control_effectiveness'])),2)
            result.append({**r,'residual_risk':score,'owner':'Security Programme Owner'})
        result.sort(key=lambda x:x['residual_risk'],reverse=True)
    elif lab_num==2:
        from sklearn.ensemble import IsolationForest
        import pandas as pd
        df=pd.read_csv(DATA); features=['failed_logins','new_device','geo_velocity_kmh','bytes_out_mb']
        model=IsolationForest(contamination=.25,random_state=42).fit(df[df.label=='baseline'][features])
        ev=df[df.label=='evaluate'].copy(); ev['anomaly_score']=model.decision_function(ev[features]); ev['alert']=ev['anomaly_score']<ev['anomaly_score'].quantile(.75); result=ev.to_dict('records')
    elif lab_num==3:
        for r in rows:
            reasons=[]; score=0
            for field,weight,reason in [('spf_pass',25,'SPF_FAIL'),('dkim_pass',20,'DKIM_FAIL')]:
                if r[field]=='0': score+=weight; reasons.append(reason)
            if r['reply_to_mismatch']=='1': score+=20; reasons.append('REPLY_TO_MISMATCH')
            if int(r['domain_age_days'])<30: score+=20; reasons.append('YOUNG_DOMAIN')
            score+=min(15,int(r['urgency_terms'])*4)
            action='quarantine-review' if score>=70 else 'analyst-review' if score>=35 else 'allow-monitor'
            result.append({**r,'risk_score':min(score,100),'action':action,'reason_codes':'|'.join(reasons) or 'NO_HIGH_RISK_SIGNAL'})
    elif lab_num==4:
        for r in rows:
            score=float(r['cvss'])*(.35+.65*float(r['epss']))*(1+.35*int(r['internet_exposed']))*(.6+.1*int(r['criticality']))*(.65 if int(r['compensating_control']) else 1)
            score=round(min(10,score),2); result.append({**r,'context_priority':score,'sla':'24h' if score>=8 else '7d' if score>=6 else '30d'})
        result.sort(key=lambda x:x['context_priority'],reverse=True)
    elif lab_num==5:
        for r in rows: result.append({**r,'weighted_score':2*int(r['value'])+int(r['data_readiness'])+int(r['integration'])-int(r['operating_risk'])-int(r['automation_impact'])})
        result.sort(key=lambda x:x['weighted_score'],reverse=True)
    elif lab_num==6:
        result=[{'from':rows[i]['component'],'to':rows[i+1]['component'],'risk':'indirect prompt injection' if i==1 else 'excess permission','control':'content isolation' if i==1 else 'least privilege','owner':'AI Security Owner'} for i in range(len(rows)-1)]
    elif lab_num==7:
        result=[{'epic':f'E{i}','gap_id':r['gap_id'],'owner':r['current_owner'],'metric':'evidence-backed closure rate','target':'100% by gate'} for i,r in enumerate(rows,1)]
    elif lab_num==8:
        result={'principles':['immutable evidence','versioned inference','guarded action','manual fallback'],'components':rows,'identities':{'analytics':'read-only evidence','tool_broker':'scoped actions'}}
    elif lab_num==9:
        import pandas as pd
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        df=pd.read_csv(DATA); allowed=df[df.classification=='internal']; q='phishing domains and consent lures'
        v=TfidfVectorizer(stop_words='english'); X=v.fit_transform(list(allowed.text)+[q]); scores=cosine_similarity(X[-1],X[:-1]).ravel()
        result=[{'document_id':allowed.iloc[i].document_id,'score':round(float(scores[i]),3),'citation':allowed.iloc[i].text} for i in scores.argsort()[::-1][:2] if scores[i]>=.1]
    elif lab_num==10:
        result=[{**r,'mode':'dry-run','proposed_action':'submit-for-approval' if float(r['confidence'])>=.85 else 'analyst-review','precondition':'identity-confirmed','rollback':'restore-session-and-review','blast_radius':int(r['active_sessions'])} for r in rows]
    elif lab_num==11:
        done=set(); order=[]
        while len(order)<len(rows):
            progressed=False
            for r in rows:
                deps=set(filter(None,r['depends_on'].split('|')))
                if r['id'] not in done and deps<=done:
                    order.append(r); done.add(r['id']); progressed=True
            if not progressed: raise ValueError('dependency cycle or missing dependency')
        day=0
        for r in order: result.append({**r,'earliest_start_day':day}); day+=int(r['duration_days'])
    elif lab_num==12:
        from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score
        y=[int(r['actual']) for r in rows]; p=[int(r['predicted']) for r in rows]; tn,fp,fn,tp=confusion_matrix(y,p).ravel()
        result={'tp':int(tp),'fp':int(fp),'fn':int(fn),'tn':int(tn),'precision':precision_score(y,p),'recall':recall_score(y,p),'f1':f1_score(y,p),'prevalence':sum(y)/len(y),'recommendation':'human-reviewed pilot; tune threshold and review drift weekly'}
    (EVIDENCE/'result.json').write_text(json.dumps(result,indent=2,default=str),encoding='utf-8')
    for name in OUTPUTS[lab_num]: write_output(name,result)
    return result
