swbd
====

**South West Big Data Hack/Reduce code repository.**

Please join our mailing list to discuss past and future Hack/Reduce events in the South West of England.

* http://www.meetup.com/south-west-big-data/messages/archive/

Hack/Reduce 1: Looking at Bristol through Data
==============================================
*15th/16th February 2013*

## What we made ##

We made these (and more) tools, visualizations and other things at the first SW Hack/Reduce event. Most are works in progress. If you made something at the event, or have since updated or improved something we made, please let us know.

### Death & Taxes (Life Expectancy by Bristol Wards) ###
###### Live demo
* http://deathandtaxes.herokuapp.com/

###### GitHub Repo
* https://github.com/MRdNk/DeathAndTaxes

(data from Wardley 2000)

### Bristol Ward Map ###
By Simon Price. In Javascript.
###### Site
* http://mrdnk.github.com/BristolWardMap/

###### Source code
* https://github.com/MRdNk/BristolWardMap
* https://fluff.bris.ac.uk/fluff/u2/ecsnp/r9j1wtwEttlNqcuzIUBn3wEIL/ (hackreduce.zip available until Mon Mar 4)

(data from Ordnance Survey OS OpenData)

### Bristol Data as JSON ###

###### Github Repo
* git@github.com:MRdNk/swbd.git
* https://github.com/MRdNk/swbd

###### Site
* http://bristol-data.herokuapp.com/
(data from various sources)

### Word frequencies in historic Bristol obituaries ###

We tackled this from a couple of angles.

Firstly, this Javascript code by Mark Heseltine produces a word cloud visualization. Users can select the month and year of the source texts interactively. Licensed as open source under the Creative Commons Attribution 3.0 Unported License.
###### Github repo.
*  https://github.com/markheseltine/southwestbigdata/tree/master/HackReduce01

Chris Bailey's pair of Python scripts, mapper.py and reducer.py [(in the literary-obituaries directory of this repository)](https://github.com/paulharwood/swbd/tree/master/literary-obituaries) can be used as a Mapper and Reducer in Hadoop to count word frequencies in the body of the articles, omitting the metadata. scrape_obituaries.py (in the same place) can be used to obtain a similar corpus of obituaries from a 21st century newspaper website, which you can compare with the historical data.

(data from Wardley 2000)

Common resources (usual suspects) 
------------------------------------------------------
* http://ias.bristol.gov.uk/IAS/explorer/resources/

* https://dev.twitter.com/docs/api

* http://developers.facebook.com/docs/reference/api/

* http://webscope.sandbox.yahoo.com/index.php

* http://freebase.com (also on AWS as a raw dump)

Themes
======

### People ###

* http://aws.amazon.com/datasets/2320

* http://data.gov.uk/dataset/youth_cohort_study_longitudinal_study_of_young_people_in_england_-_office_for_standards_in_education

* http://data.gov.uk/dataset/england-nhs-connecting-for-health-organisation-data-service-data-files-of-nhs-organisations

* http://data.gov.uk/node/11920

* https://www.nomisweb.co.uk/

* https://www.nomisweb.co.uk/query/construct/components/stdListComponent.asp?menuopt=12&subcomp=100

* http://www.google.com/publicdata/directory#!q=UK&dp=Department+for+Work+and+Pensions,+via+NOMIS

### Weather ###

* http://aws.amazon.com/datasets/2759

* http://geosci.uchicago.edu/~rtp1/PrinciplesPlanetaryClimate/Data/dataPortal.html

### Traffic ###


### Finance ###

* http://data.gov.uk/dataset/coins

Resources
=========

###### Github Cheatsheet

* https://na1.salesforce.com/help/doc/en/salesforce_git_developer_cheatsheet.pdf

###### AWS Cheatsheet

* http://ged.msu.edu/angus/tutorials/starting-your-cloud-system.html

References and thanks
=====================

Wardley, P. (2000) (editor). *[Bristol historical resource CD-ROM](http://historycd.uwe.ac.uk/)*, University of the West of England, Bristol. ISBN 1860433081 [OCLC Number 49008697](http://www.worldcat.org/title/bristol-historical-resource/oclc/49008697)

(Readers at the UWE Library can access the CD at http://eprints.uwe.ac.uk/15092/ and other local libraries also have copies.)

[Dr. Peter Wardley](http://people.uwe.ac.uk/Pages/person.aspx?accountname=campus%5cp-wardley) of the University of the West of England kindly loaned us his Bristol Historical Resource CD ROM for the first SWBD Hack/Reduce event.

Map data from Ordnance Survey's [OS OpenData products](https://www.ordnancesurvey.co.uk/opendatadownload/products.html). Contains Ordnance Survey data © Crown copyright and database right 2013