import urllib.request

def cleanFloat(input):
    return float(input.strip())

def writeValue(value, lineEnd=False):
    if lineEnd:
        outputFile.write(f'{str(value)}in\n')
    else:
        outputFile.write(f'{str(value)}in ')
    
    
airfoilURL = input("""Input URL of "Selig format dat file" from airfoiltools.com: """)

response = urllib.request.urlopen(airfoilURL).read().decode('utf-8')

invertWing = True
setRightPlane = True

siteLines = response.split('\n')

title = siteLines.pop(0)

outputFile = open(f"{title}.txt", 'w+')

for line in siteLines:
    if line:
        line = line.strip()

        numbers = line.split()
        
        inputX = (cleanFloat(numbers[0]))
        inputY = (cleanFloat(numbers[1]))
        
        if invertWing:
            inputY *= -1.0
        
        if setRightPlane:
            inputX *= -1.0
            writeValue(0)
            writeValue(inputY)
            writeValue(inputX, True)
            
outputFile.close()

print(f"Text file generated for airfoil {title}")