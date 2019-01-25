from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'wordcount/index.html')

def about(request):
    return render(request,'wordcount/about.html')

def result(request):
    from konlpy.tag import Okt
    twitter = Okt()
    words = {}
    data = twitter.pos(str(request.GET['fulltext']), norm=True, stem=True)
    for datum in data:
        
        if not datum[1] == 'Josa' and not datum[1] == 'Punctuation' and not datum[1] == 'Conjunction' and not datum[1] == 'Number' and not datum[1] == 'Suffix':
            if not datum in words:
                words.update({datum:1})
            else:
                words[datum] += 1
    print(words)
        # print("name : ", name, ", tag : ", tag)

    return render(request,'wordcount/result.html', {'words':words})