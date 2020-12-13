# SR&ED Record Generator code at Oct 13-20  SBJ
# Creates the following records from csv sources:
# 10 github - from github report

# 20 email  - csv was exported from Thunderbird.

# 21 Zoom invitation email messages
#       21	0	0	0	0	D	2019-04-15	F	1	T	5	S	Please join Zoom meeting in progress

# 30 telephone calls - From Rogers

# 40 Zoom meetings - derived from email invitations

# 50 Contractor hours - from spreadsheet

# 60 Employee hours - from program & spreadsheet
#       timesheetTuple = (rectype, 0, dayString, name, empno, project, hours, workType, workDesc )



import csv
from time import perf_counter as my_timer
from datetime import datetime
import datetime
import collections
import random
import uuid


#Line = collections.namedtuple('Line', '')


# =============================================================================
# A function to convert the date format from '6/13/2019 14:32' to yyy-mm-dd
#                                             01234567890123456789012
def date_convert1 (dt):
    year=(dt[slice (6,10)])      #YYYY
    day = dt[slice (3,5)]
    month = dt[slice  (2)]
    if month[1]=='/':           # If this is a 1-digit month
        month = month.rjust(3,'0')      # leading 0 pad for 1-digit months
        month = month[slice(2)]
        year=(dt[slice (5,9)])      #YYYY
        day = dt[slice (2,4)]
    return (year + '-'+ month + '-' + day)        # yyyy-mm-dd



# =============================================================================
# A function to convert the date format from 'Fri Nov 3 15:05:37 2017 ' to yyy-mm-dd
#                                             01234567890123456789012
def date_convert (dt):
    dt1=(dt[slice (20,24)])      #YYYY
    day = dt[slice (8,10)]
    if day[1] == ' ':            # Test for single-digit day #
        dt1=(dt[slice (19,23)])  #YYYY slide the slice to preserve the MSD of the year
        day = day.rjust(3,'0')      # Add a 0 to right-justify a single digit Day
    return (dt1 + '-'+ str(month_string_to_number(dt[slice (4,7)])) + '-' + day)        # yyyy-mm-dd

# =============================================================================
# A function to convert month letters to number

def month_string_to_number(string):
    m = {
        'jan':'01',
        'feb':'02',
        'mar':'03',
        'apr':'04',
        'may':'05',
        'jun':'06',
        'jul':'07',
        'aug':'08',
        'sep':'09',
        'oct':10,
        'nov':11,
        'dec':12
    }
    s = string.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')

# =============================================================================
# A function to convert email addresses to code numbers

def emailName(name):   #

    if 'stevej' in name or 'steve.jackson' in name or 'sbj314' in name or 'SBJ314' in name or 'STEVEJ' in name:
        return 1
    if 'bobj' in name or 'Robert Jackson' in name or 'robertjackson' in name:
        return 2
    if 'chrisj' in name or 'chrisbjackson' in name or 'chrisj' in name:
        return 3
    if 'jamie' in name or 'Jamie Rodgers' in name:
        return 4
    if 'markdaugela' in name or 'Daugela' in name:
        return 5
    if 'Vyacheslav' in name:
        return 6
    if 'Jim Clements' in name or 'JimC@' in name or 'Yan, Frank' in name:
        return 7
    if 'Tom Tranmer' in name:
        return 8
    if 'Amr Awad' in name:
        return 9
    if 'phil.mccoleman' in name:
        return 10
    if 'buyandsell.gc.ca' in name:
        return 11
    if 'david.christopherson' in name:
        return 12
    if 'Prabhas Mishra' in name:
        return 13
    if 'Duguid' in name or 'octopusred' in name  or 'lauraroberts30' in name:
        return 14
    if 'Stefan Wolpers' in name:
        return 15
    if 'DZone Daily Digest' in name  or 'dzone.com' in name or 'DZone Webinars' in name:
        return 16
    if 'noreply@github.com' in name:
        return 17
    if 'John Matecsa' in name:
        return 18
    if 'drrob@robertscullion' in name or 'Rob.Nicholson' in name:
        return 19
    if 'terry.branch' in name:
        return 20
    if 'Peter Saeglitz' in name:
        return 21
    if 'Udemy' in name:
        return 22
    if 'Dan Bader' in name or 'realpython' in name:
        return 23
    if 'Slack' in name:
        return 24
    if 'success@hologram' in name:
        return 25
    if 'Dropbox' in name:
        return 26
    if 'Upwork' in name or 'upwork' in name:
        return 27
    if 'iotnow' in name:
        return 28
    if 'Atlassian' in name:
        return 29
    if 'Chargebee' in name:
        return 30
    if 'nginx' in name:
        return 31
    if 'veeam' in name:
        return 32
    if 'icloud' in name:
        return 33
    if 'brighttalk' in name:
        return 34
    if 'infoq' in name:
        return 35
    if 'machinedesign' in name:
        return 36
    if 'channelfut' in name:
        return 37
    if 'carbonblack' in name:
        return 38
    if 'gremlin' in name:
        return 39
    if 'qt.io' in name:
        return 40
    if 'storagecraft' in name:
        return 41
    if 'pycoders' in name:
        return 42
    if 'researchgate' in name:
        return 43
    if 'confluent' in name:
        return 44
    if 'magner.com' in name:
        return 45
    if 'bobsardinski' in name:
        return 46
    if 'john@jltax' in name:
        return 47
    if 'bangsfuels' in name:
        return 48
    if 'tibco.com' in name:
        return 49
    if 'sheldongroup' in name:
        return 50
    if 'david.carter' in name:
        return 51
    if 'imboden' in name or 'telus.com' in name:
        return 52
    if 'russdoucet' in name:
        return 53
    if 'psac-afpc' in  name or 'pipsc.ca' in name:
        return 54
    if 'mysocialmediapartner' in name:
        return 55
    if 'Ransomcloud' in name:
        return 56
    if 'okta.com' in name:
        return 57
    if 'FloreantHackDemo' in name:
        return 58
    if 'Enterprise.nxt' in name:    #Hewlett Packard
        return 59
    if 'kevinbrowne' in name:    # Prof Browne
        return 60
    if 'arthur.wiebe' in name:
        return 61
    if 'kernleysv' in name:
        return 62
    if 'j.harris@ieee' in name:
        return 63
    return 99               # Unrecognized names are called 99

# =============================================================================
# A function to flag Canadian holidays in I-Tech's 2018-19 fiscal year

hols = ['2018-08-03', '2018-10-08', '2018-11-11', '2018-12-25', '2018-12-26', '2019-01-01', '2019-02-18', '2019-04-18', '2019-04-22', '2019-05-20', '2019-07-01', '2019-08-05']



def holidayList(day):   #return 1 iff day is NOT a holiday

    dayy = day.strftime("%Y-%m-%d")     #Convert day to a string
    #    print (type (dayy), dayy)
    if dayy in hols:
        return 0
    return 1


# =============================================================================

def archive(record):

    """A function to append a new list DS RECORD list to the eternal Archive txt file."""
    #
    #    with open ("archive50.txt", "a", newline='') as arch:

    writer = csv.writer(arch, delimiter='\t')
    writer.writerow(record)
    return



# =============================================================================

start_time = my_timer()

arch = open ("archive50.txt", "w+", newline='')

# A routine to create GitHub Push records from the Github.csv file.

with open("Github.csv", newline='')  as f:
    rectype = '10'      # GitHub Records
    rdr = csv.reader(f, delimiter = "\t")
    for row in rdr:
        date1 = date_convert (row[1])
        # x = slice (4,10)
        # y = slice (20,24)
        # print (date1)
        topic = row[0]
        poster = row[3]
        activity = row[4]

        newUUID = uuid.uuid4()



        #record = (rectype, 0, newUUID, '00000000-0000-0000-0000-000000000000','00000000-0000-0000-0000-000000000000', 'D', date1, 'T',topic, 'F',poster, 'A', activity)  #Convert List to a String
        record = (rectype, 0, 'D', date1, 'T',topic, 'F',poster, 'A', activity)  #Convert List to a String

        archive (record)                #Append this String to the archive.txt file!



# =============================================================================

# A routine to create email records from the Mail.csv file. This was exported from Thunderbird.

with open("Mail.csv", newline='')  as f:
    rdr = csv.reader(f, delimiter = ",")
    rectype = '20'          # email records
    for row in rdr:

        subject = row[0]
        fromm = row[1]
        fromm = emailName(fromm)

        to = row[2]
        to = emailName(to)

        date = row[3]

        #newUUID = uuid.uuid4()
        newUUID  = '0'


        record = (rectype, 0, newUUID, '0','0', 'D',date, 'F',fromm, 'T',to, 'S',subject)  #Convert List to a String

        archive (record)                #Append this String to the archive.txt file!


# =============================================================================

# A routine to create email records from the Zoom invitation messages.csv file. This was exported from Thunderbird.

with open("Zoom invitation messages.csv", newline='')  as f:
    rdr = csv.reader(f, delimiter = ",")
    rectype = '21'          # Zoom email records
    for row in rdr:

        subject = row[0]
        fromm = row[1]
        fromm = emailName(fromm)

        to = row[2]
        to = emailName(to)

        date = date_convert1 (row[3])

        #newUUID = uuid.uuid4()
        newUUID  = '0'


        record = (rectype, 0, newUUID, '0','0', 'D',date, 'F',fromm, 'T',to, 'S',subject)  #Convert List to a String

        archive (record)                #Append this String to the archive.txt file!

        #Now create a Zoom meeting record, type 40!

        record = ('40', 0, newUUID, '0','0', 'D',date, 'F',fromm, 'T',to, 'S',subject)

        archive (record)                #Append this String to the archive.txt file!




# =============================================================================

# A routine to create phone records from the the PhoneHours Oct 14-20.txt file. This was downloaded from Rogers.com

with open("PhoneHours Oct 14-20.txt", newline='')  as f:
    rdr = csv.reader(f, delimiter = "\t")        # tab \t
    rectype = '30'          # Phone records
    for row in rdr:

        x = row[0]                  # First string in the list
        if ord(x[0]) > 200:         # Test for a reasonable character at line start
            continue                # Bypass this rogue line!

        date1 = row[0]              # Sat Nov 02
        year = row[1]              # YYYY
        time = row[2]
        from_city=row[3]
        to_number = row[4]
        to_city = row[5]
        duration = row[6]
        month = str (date1[slice(4,8)])
        month = str(month_string_to_number(month)) # month
        day = date1[slice(8,10)]

        date = (year + '-' + month + '-'+ day)

        #newUUID = uuid.uuid4()
        newUUID  = '0'


        record = (rectype, 0, newUUID, '0','0', 'D',date, 'F',from_city, 'T', to_number, 'D',duration)  #Convert List to a String

        archive (record)                #Append this String to the archive.txt file!





# =============================================================================

# A routine to create JSR's contractor timesheets from a real source txt file

with open("JSRHRS.txt", newline='')  as f:
    rdr = csv.reader(f, delimiter = "\t")
    rectype = '50'              # Contractor Hours record
    project = '02'
    for row in rdr:

        date = row[0]
        hrs = row[1]
        matter = row[2]
        inv = row[3]

        #newUUID = uuid.uuid4()
        newUUID = '0'

        if hrs != '':
            record = (rectype, 0, newUUID, '','0', date, 'JSR', project, hrs, inv, matter)  #Convert List to a String
            archive (record)                #Append this String to the archive.txt file!



# =============================================================================

# A Routine to create RAJ's daily timesheet record
# Aug 31-20 SBJ

# Sept 1-18 is a Saturday (5). Monday is 0.
# 1	0	9d88c2d7-f4fa-4858-808c-2ad457f353d7	00000000-0000-0000-0000-000000000000	00000000-0000-0000-0000-000000000000	139	CONN MOD JACK RJ45 8-8 VERT PCB AMP	5520259-4 	TYCO	CN


rectype = '60'    # Employee Hours record
day = datetime.date(2018, 8, 31)    #The day before the 2019 FY starts
dow = 4     # Saturday - 1

for i in range (365):
    # Sept 1-18 is a Saturday (5). Monday is 0.
    day += datetime.timedelta(days=1)
    dow += 1
    if dow == 7:
        dow = 0

    if dow in range (0,5):

        if holidayList(day):
            # newUUID = uuid.uuid4()
            # uuid0 = '00000000-0000-0000-0000-000000000000'
            newUUID = '0'
            uuid0 = '0'

            dayString = day.strftime("%Y/%m/%d")
            name = 'RAJ'
            empno = '01'
            project = '02'
            workType = '10'
            hours = '05'
            workDesc = '22'
            #timesheetTuple = (rectype, 0, str(newUUID), uuid0, uuid0, dayString, name, empno, project, hours, workType, workDesc )
            timesheetTuple = (rectype, 0, dayString, name, empno, project, hours, workType, workDesc )
            #        print (timesheetTuple)
            archive(timesheetTuple)

# =============================================================================
# Now reoprt the elapsed time

end_time = my_timer()

print('\n' "Duration was {} seconds.".format(end_time - start_time))
