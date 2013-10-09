from lstory.models import Story
from onon.models import Feature, NonfeatureContent, Zahltag
from django.views.generic.simple import direct_to_template

def index(request, template='onon/index.html'):
    stories = Story.objects.filter(published__isnull=False)
    features = Feature.objects.all()

    all_features = [x.main_story for x in features if x.main_story] + [x.other_story for x in features if x.other_story]

    nonfeature = NonfeatureContent.objects.all()
    zahltage = Zahltag.objects.all()
    zahltage = [x for x in zahltage if x not in all_features]
    
    stories = [x for x in stories if x not in all_features]

    timeline = sorted(list(features)+list(nonfeature),key=lambda x: x.date, reverse=True)

    return direct_to_template(request, template, {
        'stories': [x for x in stories if not x.retired],
        'retired': [x for x in stories if x.retired],
        'timeline': timeline,
        'zahltage': zahltage,
    })
