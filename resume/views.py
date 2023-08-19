from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Profile,Account,Experiance,SSLC,PUC,University,Project,Skill
from django.contrib.auth.hashers import make_password,check_password
from datetime import datetime
from django.template.loader import get_template
from xhtml2pdf import pisa 



import pdfcrowd
from django.template.loader import render_to_string

# Create your views here.
def resume(request):
    return render(request,'home.html')


def form(request):
    return render(request,'form.html')

def signin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.check_user(email)
        if user:
            if check_password(password,user.password):
                request.session['user']=email
                return render(request,'home.html')
            else:
                error="wrong password entered"
                return render(request,'signin.html',{'error':error})
        else:
            error="wrong email or password entered"
            render(request,'signin.html',{'error':error})
    return render(request,'signin.html')

def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password == cpassword:
            password=make_password(password)
            user=User(user=email,password=password)
            user.save()
            return render(request,'signin.html')
        else:
            error="password and confirmation password does not match"
            return render(request,'signup.html',{'error':error})
    return render(request,'signup.html')


def final(request):
    email='xyz@gmail.com'
    if request.method=='POST':
        
        user=User.check_user(email)
        print(user)
        
        img=request.FILES.get('profile1')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        pnumber=request.POST.get('pnumber')
        zip=request.POST.get('zip','')
        city=request.POST.get('city')
        address=request.POST.get('address')
        objective=request.POST.get('obj')
        profile=Profile(image=img,fname=fname,lname=lname,pnumber=pnumber,zip=zip,city=city,address=address,objective=objective,user=user)
        try:
            declaration=request.POST.get('declaration')
            profile.declaration=declaration
        except:
            pass
       
        profile.save()
        
        
        email=request.POST.get('email')
        github=request.POST.get('github')
        linkdin=request.POST.get('linkdin')
        
   
        facebook=request.POST.get('facebook','')
   
        pineterest=request.POST.get('pineterest','')
        account=Account(email=email,linkdin=linkdin,github=github,facebook=facebook,pinterest=pineterest,user=user)
        account.save()
        
        exp=request.POST.get('exp')
        exp=Experiance(exp=exp,user=user)
        exp.save()
        
        
        sname=request.POST.get('sname')
        syear=request.POST.get('syear')
        sboard=request.POST.get('sboard')
        smarks=request.POST.get('smarks')

        institute=request.POST.get('sint')
        sslc=SSLC(name=sname,year=syear,board=sboard,institute=institute,marks=smarks,user=user)
        sslc.save()
        
        
        pname=request.POST.get('pname')
        pyear=request.POST.get('pyear')
        pboard=request.POST.get('pboard')
        pmarks=request.POST.get('pmarks')
        institute=request.POST.get('pint')
        puc=PUC(name=pname,year=pyear,board=pboard,marks=pmarks,institute=institute, user=user)
        puc.save()
        
        
        uname=request.POST.get('uname','')
        uyear=request.POST.get('uyear','')
        uboard=request.POST.get('uboard','')
        umarks=request.POST.get('umarks','')
        institute=request.POST.get('uint','')
        university=University(name=uname,year=uyear,board=uboard,marks=umarks,institute=institute,user=user)
        university.save()
           
             
        sskill=request.POST.get('sskill')
        tskill=request.POST.get('tskill','')
        language=request.POST.get('lang')
        skill=Skill(softskill=sskill,techskill=tskill,lang=language,user=user)
        skill.save()
        
        
        sskill = sskill.split(",")
        tskill=tskill.split(",")
        language = language.split(",")
        
        
        
        time=datetime.now()
        
        i=1
        list=[]
        while True:
            try:
                prjname=request.POST.get('projectName' + str(i))
                prjdesc=request.POST.get('projectdesc' + str(i))
                prjlink=request.POST.get('projectlink' + str(i))
                prj=Project(name=prjname,description=prjdesc,link=prjlink,user=user)
                prj.save()
                dict={'prjname':prjname,'prjdesc':prjdesc,'prjlink':prjlink}
                list.append(dict)
                i=i+1
            except:
                break    
            
        btn=request.POST.get('btn')
        
        
        
        
                # settings.py
        import cloudinary
        cloudinary.config(
            cloud_name='dxy8dt7jb',
            api_key='748313451189741',
            api_secret='9yrV4GnuCJuqKfMvv9Y8wfPvBhI'
        )
        # views.py

        import cloudinary.uploader
        
        # Upload the image to Cloudinary
        upload_result = cloudinary.uploader.upload('media\\attachments\\uploads\\' + img.name)
        # Get the URL of the uploaded image
    
        image_url = upload_result.get('secure_url', '')
        
            # https://console.cloudinary.com/console/c-9058fb4377870bf56823c323430ddc/getting-started
            
            
        
        
        if btn == 'download':
            api_key = 'ce544b6ea52a5621fb9d55f8b542d14d'

            # Replace 'YOUR_USERNAME' with your pdfcrowd username
            username = 'demo'

            # # Replace 'YOUR_HTML_CONTENT' with the actual HTML content you want to convert
            # html_content = 'resume.html'

                # Replace 'path/to/your/html_file.html' with the actual path to your HTML file
            html_file_path = r'C:\Users\HP\esite\esite\resume\templates\resume.html'
            context_data = {
            'profile':profile,'sskill':sskill,'tskill':tskill,'language':language,'university':university,'sslc':sslc,'puc':puc,'exp':exp,'account':account,'list':list,'time':time,'img_url':image_url
            # Add more context variables as needed
            }

            html_content = render_to_string(html_file_path, context_data)
            
            
            
        
            
            
            
            # Create the pdfcrowd client
            client = pdfcrowd.HtmlToPdfClient(username, api_key)

            # Create a response object to store the PDF
            pdf_response = HttpResponse(content_type='application/pdf')
            pdf_response['Content-Disposition'] = 'attachment; filename="output.pdf"'

            try:
                pdf_page_size = 'A2'
                client.setPageSize(pdf_page_size)

            
                # Convert the rendered HTML content to PDF and write it to the response
                client.convertStringToStream(html_content, pdf_response)
            except pdfcrowd.Error as why:
                # Handle any errors that may occur during conversion
                pdf_response = HttpResponse('An error occurred: {}'.format(why), content_type='text/plain')

            return pdf_response
            
        else:
            
            
            
            
            






            return render(request,'resume.html',{'profile':profile,'sskill':sskill,'tskill':tskill,'language':language,'university':university,'sslc':sslc,'puc':puc,'exp':exp,'account':account,'list':list,'time':time,'img_url':image_url})
        
    return render(request,'resume.html')







    
    
    
    


def split_html_into_parts(html_content):
    total_length = len(html_content)
    midpoint = total_length // 2

    part1 = html_content[:midpoint]
    part2 = html_content[midpoint:]

    return part1, part2








