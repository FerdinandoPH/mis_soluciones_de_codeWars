def purge_text(text):
    remove_chars = str.maketrans(',./<>?;:\"[]{}\\|`~!@#$%^&*()_+-=',' '*31)
    text = text.translate(remove_chars)
    
    text = text.lower()
    
    apostrophes_to_delete=[]
    for i in range(0,len(text)):
        if text[i]=="\'":
            try:
                if not text[i-1].isalpha() and not text[i+1].isalpha():
                    apostrophes_to_delete.append(i)
            except IndexError:
                apostrophes_to_delete.append(i)
    for apostrophe in apostrophes_to_delete:
        if apostrophes_to_delete.index(apostrophe)!=len(text)-1:
            text=text[:apostrophe]+"*"+text[apostrophe+1:]
        else:
            if len(text)==1:
                text=""
            else:
                text=text[:apostrophe]
    text=text.replace('*','')
    return text
def top_3_words(text):
    print("Original text:",text)
    print("Cleaned text:",purge_text(text))
    words={}
    for word in purge_text(text).split():
        words[word]=words.get(word,0)+1
    print(words)
    print(sorted(words.values(),reverse=True)[:3])
    top_3=sorted(words,key=words.get,reverse=True)[:3]
    print(top_3)
    return top_3
if __name__=="__main__":
  print(top_3_words("In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income."))
  print(top_3_words("'nvguR; .?SMQFQ;-?MDlucCaE!VdSslMs__._;IpUJNsh/:.;VdSslMs.?;.?ISFnn..;kZCxPaQQG :_MDlucCaE ?-!'nvguR- -,.'nvguR.!?,MDlucCaE,!SMQFQ,,-_!sYXBssu,::?;sYXBssu:/_ ;VFaLXwmmP;_kZCxPaQQG_;SMQFQ;,-!/VFaLXwmmP??-/MDlucCaE_gSNDCyACZf ?SMQFQ?,VdSslMs,.-.;SMQFQ!:-_-YQXHr-_!_.IpUJNsh VdSslMs,VdSslMs_./._gSNDCyACZf:!!!VFaLXwmmP?:.VdSslMs/_ sYXBssu:IpUJNsh.:;SMQFQ ?,!:VFaLXwmmP_.,IpUJNsh:-?IpUJNsh-MDlucCaE_/_MDlucCaE--,SMQFQ/;:ISFnn VFaLXwmmP ;ISFnn:,_/!MDlucCaE,?,SMQFQ:!VdSslMs-?kZCxPaQQG SMQFQ?'KXUNpjS,;?  VdSslMs,'nvguR:gSNDCyACZf:;sYXBssu?,VdSslMs-!?SMQFQ_/:gSNDCyACZf?-/;_VdSslMs kZCxPaQQG?IpUJNsh:sYXBssu IpUJNsh:--sYXBssu-,MDlucCaE;-!?MDlucCaE:!.VFaLXwmmP!!!?_ISFnn-:VdSslMs-?:VdSslMs?!VFaLXwmmP-_-//'KXUNpjS!:-gSNDCyACZf?-.?-SMQFQ:?; gSNDCyACZf:-/;:sYXBssu /:-gSNDCyACZf;.??/MDlucCaE?'KXUNpjS..'nvguR?  ;kZCxPaQQG/:IpUJNsh:,:/MDlucCaE.; ?;kGeoWPVW:!/-VFaLXwmmP/VFaLXwmmP_!/gSNDCyACZf?;gSNDCyACZf VFaLXwmmP,.!gSNDCyACZf:IpUJNsh/_ SMQFQ!:.sYXBssu/,VFaLXwmmP_?SMQFQ:VdSslMs// ?VFaLXwmmP?sYXBssu, !/sYXBssu;-VFaLXwmmP!?_kZCxPaQQG,IpUJNsh/?-:'nvguR:ISFnn/,-sYXBssu.-/:IpUJNsh/_,.'KXUNpjS :IpUJNsh/!kZCxPaQQG!.-IpUJNsh!kZCxPaQQG/'nvguR/.VdSslMs!;/;'nvguR.;IpUJNsh,!'KXUNpjS_-?_,kZCxPaQQG-SMQFQ.,MDlucCaE; _;kGeoWPVW_,!IpUJNsh MDlucCaE ,IpUJNsh.,, ,sYXBssu?/.:!VdSslMs/,'nvguR! :'nvguR:_.;'nvguR:!:sYXBssu,!/'nvguR:,;:sYXBssu!_gSNDCyACZf;-/!:VdSslMs.:-?ISFnn :-/?MDlucCaE/_ISFnn ?IpUJNsh;.//SMQFQ:_IpUJNsh_gSNDCyACZf,. ?sYXBssu,-VdSslMs/.!:/ISFnn;_.!_SMQFQ_/MDlucCaE;__-_'KXUNpjS.?_:?sYXBssu.sYXBssu:kZCxPaQQG_.VdSslMs-kZCxPaQQG??SMQFQ-MDlucCaE_-?!'KXUNpjS/sYXBssu.::!/gSNDCyACZf,:kGeoWPVW-:VFaLXwmmP???.?sYXBssu:-/:/gSNDCyACZf-!/ISFnn,_'nvguR!'nvguR/!._VdSslMs.? //'nvguR/-!;'nvguR-;;;-VdSslMs!.?:MDlucCaE ::_SMQFQ,-_VdSslMs; gSNDCyACZf:!?'nvguR?'nvguR,-/,'nvguR?-'KXUNpjS.!!-ISFnn ;kZCxPaQQG_MDlucCaE?_VFaLXwmmP.!-_ 'nvguR!kZCxPaQQG:: -ISFnn; ;'nvguR_SMQFQ?:/!'KXUNpjS,.:?_sYXBssu,; _ IpUJNsh VdSslMs_ kZCxPaQQG;MDlucCaE:_! YQXHr .VdSslMs _?-MDlucCaE:,/ISFnn,/VFaLXwmmP,?,;kZCxPaQQG,? gSNDCyACZf--.;VdSslMs:; .?SMQFQ_.:;;VdSslMs!MDlucCaE-!'nvguR_-,-kGeoWPVW./,VFaLXwmmP!/'nvguR,;;gSNDCyACZf!/!ISFnn/_!._VdSslMs.,.!gSNDCyACZf:sYXBssu.MDlucCaE_-/sYXBssu/,! ISFnn-'KXUNpjS!kZCxPaQQG!:SMQFQ //kGeoWPVW,?:sYXBssu!!;sYXBssu-!kZCxPaQQG IpUJNsh- ISFnn/__!'KXUNpjS/'nvguR!'nvguR?:.?SMQFQ!gSNDCyACZf!IpUJNsh;?:?.'KXUNpjS;;_/SMQFQ-IpUJNsh  -kGeoWPVW!,gSNDCyACZf;: sYXBssu!_'KXUNpjS./ VdSslMs:-:-MDlucCaE,_?gSNDCyACZf:VdSslMs::?.gSNDCyACZf,.,-/SMQFQ?.'nvguR SMQFQ.-'KXUNpjS,:IpUJNsh.;-,,VdSslMs!!?SMQFQ:!_/'KXUNpjS/;.-;SMQFQ sYXBssu:  ?VFaLXwmmP,_.;hHbacMpoH,_//SMQFQ.-;gSNDCyACZf:?; gSNDCyACZf:sYXBssu_:/ISFnn-- _:gSNDCyACZf_MDlucCaE. , :gSNDCyACZf--:/sYXBssu;-'KXUNpjS.-::/'KXUNpjS?:!SMQFQ:-;!VdSslMs/.;;MDlucCaE,;_!ISFnn! IpUJNsh;gSNDCyACZf sYXBssu:.,,MDlucCaE!gSNDCyACZf_SMQFQ gSNDCyACZf/,kGeoWPVW--_;?"))