# I have created this file on my own --- Osama
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home page")


def analyze(request):
    # yeh text ka name humne index.html ke form mai text area ke name attribute se lia he

    global analyzed, countchar
    text1 = request.POST.get('textarea', 'default')
    print(text1)
    while text1 != '':
        analyze1 = request.POST.get('analyze', 'off')
        captialize1 = request.POST.get('fullcaps', 'off')
        newlineremover1 = request.POST.get('newlineremover', 'off')
        extraspaceremover1 = request.POST.get('extraspaceremover', 'off')
        charcount1 = request.POST.get('charcount', 'off')
        if analyze1 != 'on' and captialize1 != 'on' and newlineremover1 != 'on' and extraspaceremover1 != 'on' and charcount1 != 'on':
            return HttpResponse("<h1>Please select any operation and try again</h1>")
        else:
            print(charcount1)
            print(extraspaceremover1)
            print(newlineremover1)
            print(analyze1)
            print(captialize1)
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            if analyze1 == 'on':
                for i in punctuations:
                    if i in text1:
                        text1 = text1.replace(i, "")
                analyzed = text1
            else:
                analyzed = text1

            if newlineremover1 == 'on':
                print(text1)
                for i in text1:
                    if i == "\n" or i == "\r":
                        text1 = text1.replace(i, "")
                        print(text1)
                    else:
                        pass
                analyzed = text1
                print(analyzed)

            else:
                analyzed = analyzed

            if captialize1 == 'on':
                analyzed = analyzed.upper()
            else:
                analyzed = analyzed

            # if extraspaceremover1 == 'on':
            #     analyzed = analyzed.replace("  ", "")
            # else:
            #     analyzed = analyzed

            if extraspaceremover1 == 'on':
                words = analyzed.split()
                no_space_Word = []
                for word in words:
                    if word != "":
                        no_space_Word.append(word)

                analyzed = " ".join(no_space_Word)

            if charcount1 == 'on':
                countchar = len(analyzed)
            else:
                countchar = "Sorry"

            abc = {'purpose': 'Remove Punctuation', 'analyze_text': analyzed, 'captext': 'Capitalize Text',
                   'countchar': countchar}
            return render(request, 'analyze.html', abc)
    else:
        return HttpResponse("<h1>Please enter some text<h1/>")
