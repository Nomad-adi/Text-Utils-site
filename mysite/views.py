#my file
from django.http import HttpResponse
from django.shortcuts import render


def get_html_data(request):
    return render(request, 'index.html')


def analyzed(request):
    text = request.POST.get('text','default')
    remove_punc = request.POST.get('removepunc','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    capt = request.POST.get('capitalized','off')
    newline_rm = request.POST.get('newline_rmv','off')
    extraSpace_rm = request.POST.get('extraSpace_rmv','off')
    ch_cnt = request.POST.get('ch_counter','off')

    # removing punctuations
    if not remove_punc:

        analyzed =""
        for ch in text:
            if ch not in punctuations:
                analyzed = analyzed+ch
        text = analyzed
        parms = {'heading': 'Remove Punctuation', 'analyzed_text':text}

    if not capt:
        #capitalized the text
        analyzed = text.upper()
        parms ={"heading":'Capitalized Text', 'analyzed_text':analyzed}
        text = analyzed
        
         
    if not newline_rm:
        analyzed=''
        for ch in text:
            if ch != '\n' or ch!='\r':
                analyzed = analyzed+ch
                print(analyzed)
        
        parms ={"heading":'NewLine Remover', 'analyzed_text':analyzed}
        text = analyzed
    

    if not extraSpace_rm:
        analyzed=''
        for i, ch in enumerate(text):
            if text[i] == ' ' and text[i+1]==' ':
                pass
            else:
                analyzed = analyzed+ch
         
        parms ={"heading":'Extra Space Remover', 'analyzed_text':analyzed}
        text = analyzed 

    if not ch_cnt :
        cnt = 0
        for ch in text:
            if ch.isalpha():
                cnt = cnt+1
        text_and_cnt = f"{text} : Total count of character are {str(cnt)}"
        parms ={"heading":'Character Counter', 'analyzed_text':text_and_cnt}
      

    elif ch_cnt=='off' and extraSpace_rm=='off' and newline_rm =='off' and capt =='off' and remove_punc =='off':
        return HttpResponse('Please Select Any Operation and Try Again!')
        
    
    return render(request, 'result.html',parms)


