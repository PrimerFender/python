# This a simple test to compare version numbers (which are strings, but mathematically accurate)

oldVersion = "11.2.2"
newVersion = "11.3"

if(newVersion == oldVersion):
    print(newVersion + "is equal to " + oldVersion)
if (newVersion > oldVersion):
    print(newVersion + " is greater than " + oldVersion)
if (newVersion < oldVersion):
    print(newVersion + " is less than " + oldVersion)