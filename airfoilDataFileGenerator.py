import csv
import io


X = []
Y = []
filename = "naca0008.dat"

with open(filename, 'r+') as f:
    content = f.read()
    newLineIndex = content.find('\n')
    content = content[newLineIndex+1:]
    content = "X     Y" + '\n' + content

infile = io.StringIO(content)
r = csv.DictReader(infile,  dialect=csv.Sniffer().sniff(infile.read(1000)))
infile.seek(0)

X,Y = [] , []
for row in r:
    X.append(row['X'])
    Y.append(row['Y'])
print(X)
print(Y)
X = [float(i) for i in X]
Y = [float(i) for i in Y]
Z = [0.0] * len(Y)


chord = float(input("input airfoil section chord length: "))
fileExtension = input("input file extension: ")
offset = float(input("enter offset if any: "))

X = [(chord*x + offset) for x in X]
Y = [chord*y for y in Y]

temp = X.copy()
print(temp)
X = Z
Z = [1*z for z in temp]

print(X)
print(Y)
print(Z)

outputfilename = filename[0:filename.find('.') ] +"Chord" + str(int(chord)) + "offest" + str(int(offset)) + "." + fileExtension
with open(outputfilename, 'w') as f:
    writer = csv.writer(f,  dialect='excel-tab')
    writer.writerow(["X", "Y", "Z"])
    writer.writerows(zip(X, Y, Z))
