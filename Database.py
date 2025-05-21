def data_insert(name,phone_no,email,group):

    with open("database.txt","r") as f:
        line=f.readlines()
        if not line:
            id=1
        else:
            a=line[-1].strip()
            a=a.split(',')
            id=int(a[0])+1

    with open("database.txt",'a+') as f:
        f.write(f"{id},{name},{phone_no},{email},{group}\n")

def search_via_name(name):
    with open("database.txt","r") as f:
        line=f.readlines()
        result=[]
        for i in line:
            i=i.strip().split(',')
            if name.lower() in i[1].lower():
                result.append(i)

    return result

def search_via_group(group):
    with open("database.txt","r") as f:
        line=f.readlines()
        result=[]
        for i in line:
            i=i.strip().split(',')
            if group.lower() in i[-1].lower():
                result.append(i)

    return result


def delete(context):
    with open("database.txt","r") as f:
        line=f.readlines()
        result=[]
        id=1
        for i in line:
            i=i.strip().split(',')
            if (context.lower() in i[1].lower()) or (context.lower() in i[2].lower()) or (context.lower() in i[3].lower()) or (context.lower() in i[4].lower()) :
                continue
            else:
                ab=f"{id}," + ",".join(i[1:])
                result.append(ab)
                id+=1

    with open("database.txt", "w") as f:
        f.writelines(result)

a=input("Enter the value ")

if a=='data insert':
    name=input("Enter the name")
    phone_no=input("Enter the phone number")
    email=input("Enter the email address")
    group=input("Enter the group from which it belongs")
    data_insert(name,phone_no,email,group)
elif a=='search_via_name':
    name=input("Enter the name for which you want to extract all the entries")
    abc=search_via_name(name)
    print(abc)
elif a=='search_via_group':
    group=input("Enter the group for which you want to extract all the entries")
    abc=search_via_group(group)
    print(abc)
else:
    print("You are in the delete group")
    context=input("Enter the context name you want to elimante from the database.txt")
    delete(context)