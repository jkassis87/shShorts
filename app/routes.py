from flask import render_template, request, make_response
from app import app
import spur, sys

@app.route('/')
@app.route('/index')
def index():
    pagesettings = {'title': 'Index Page'}
    return render_template('index.html')


# code for the r1soft checking tool
@app.route('/r1check_results')
@app.route('/r1check', methods=['GET', 'POST'])
def r1check():
    # triggered when the submit button is pressed
    if request.method == 'POST':
    
        # prepares ssh login
        sshhost = request.form.get('sshhost')
        sshuser = request.form['sshuser']
        sshpass = request.form['sshpass']
        sshport = request.form['sshport']
        shell = spur.SshShell(hostname=sshhost, 
                        username=sshuser, 
                        password=sshpass,
                        port = sshport,
                        missing_host_key=spur.ssh.MissingHostKey.accept)
                        
        # options in ssh command
        sshhosttype = request.form['hosttype']
        sshr1server = request.form['r1server']
        
        #### START END prepares ssh commands to run
        
        # pings r1soft server
        ssh_r1ping = f"ping {sshr1server}"
        
        # gets list of installed kernel modules
        ssh_kernelver = r"uname -r"
        
        # gets list of installed kernels and modules
        ssh_kernelmods = r"rpm -qa | grep kernel"
        
        #### END prepares ssh commands to run
        
        # logs in to host, runs commands, outputs results to new window
        #with shell:
            #result = shell.run(["uptime"])
            #return(result.output)
        return render_template('r1check_results.html', 
                ssh_r1ping=ssh_r1ping, 
                ssh_kernelver=ssh_kernelver, 
                ssh_kernelmods=ssh_kernelmods)
        
    return render_template('r1check.html', 
        title='R1soft Connection Checker')


# code for the large files and folders checking tool
@app.route('/diskcheck_results')
@app.route('/diskcheck', methods=['GET', 'POST'])
def diskcheck():
    # triggered when the submit button is pressed
    if request.method == 'POST':
    
        # prepares ssh login
        sshhost = request.form.get('sshhost')
        sshuser = request.form['sshuser']
        sshpass = request.form['sshpass']
        sshport = request.form['sshport']
        shell = spur.SshShell(hostname=sshhost, 
                        username=sshuser, 
                        password=sshpass,
                        port = sshport,
                        missing_host_key=spur.ssh.MissingHostKey.accept)
                        
        # options in ssh command
        ssh_minfilesize = request.form['minfilesize']
                
        with shell:
        
            #### START prepares ssh commands to run
            
            # lists all files larger than ssh_minfilesize under /home/ and /backup/
            com_largefiles = shell.run(["sh", "-c", r"find /home/ /backup/ -type f -size +" + ssh_minfilesize + " -exec ls -lh {} \; | awk {'print $5, $9'}  | sort -h"])
            str_largefiles = r"find /home/ /backup/ -type f -size +" + ssh_minfilesize + " -exec ls -lh {} \; | awk {'print $5, $9'}  | sort -h"
            
            # lists 20 largest folders under /home/ and /backup/
            com_largedirs = shell.run(["sh", "-c", r"du -Sh /home/ /backup/ | sort -rh | head -20"])
            str_largedirs = r"du -Sh /home/ /backup/ | sort -rh | head -20"
            
            #### END prepares ssh commands to run
            
            # outputs to diskcheck_results.html and renders the ssh command results
            return render_template('diskcheck_results.html', 
                                    com_largefiles=com_largefiles, str_largefiles=str_largefiles,
                                    com_largedirs=com_largedirs, str_largedirs=str_largedirs)
                
    return render_template('diskcheck.html',
        title='Disk Usage Check')


# code for the bot and WP attack checking tool
@app.route('/botwpcheck_results')
@app.route('/botwpcheck', methods=['GET', 'POST'])
def wpcheck():
    # triggered when the submit button is pressed
    if request.method == 'POST':
    
        # prepares ssh login
        sshhost = request.form.get('sshhost')
        sshuser = request.form['sshuser']
        sshpass = request.form['sshpass']
        sshport = request.form['sshport']
        shell = spur.SshShell(hostname=sshhost, 
                        username=sshuser, 
                        password=sshpass,
                        port = sshport,
                        missing_host_key=spur.ssh.MissingHostKey.accept)
                        
        #### START prepares ssh commands to run


        #### END prepares ssh commands to run
        
        # logs in to host, runs commands, outputs results to new window
        #with shell:
            #result = shell.run(["uptime"])
            #return(result.output)        
        return render_template('timecheck_results.html')
        
        
    return render_template('botwpcheck.html',
        title='Bot & WP Attack Check')


# code for the "what happened to the server around this time" checking tool
@app.route('/timecheck_results')        
@app.route('/timecheck', methods=['GET', 'POST'])
def timecheck():
    # triggered when the submit button is pressed
    if request.method == 'POST':
    
        # prepares ssh login
        sshhost = request.form.get('sshhost')
        sshuser = request.form['sshuser']
        sshpass = request.form['sshpass']
        sshport = request.form['sshport']
        shell = spur.SshShell(hostname=sshhost, 
                        username=sshuser, 
                        password=sshpass,
                        port = sshport,
                        missing_host_key=spur.ssh.MissingHostKey.accept)
                        
        #### START prepares ssh commands to run                        


        #### END prepares ssh commands to run
        
        # logs in to host, runs commands, outputs results to new window
        #with shell:
            #result = shell.run(["uptime"])
            #return(result.output)
        return render_template('timecheck_results.html')
        
    return render_template('timecheck.html',
        title='Find what happend around a certain time')


# code for the tool that runs custom commands
@app.route('/customcommand_results')        
@app.route('/customcommand', methods=['GET', 'POST'])
def customcommand():
    # triggered when the submit button is pressed
    if request.method == 'POST':
    
        # prepares ssh login
        sshhost = request.form.get('sshhost')
        sshuser = request.form['sshuser']
        sshpass = request.form['sshpass']
        sshport = request.form['sshport']
        shell = spur.SshShell(hostname=sshhost, 
                        username=sshuser, 
                        password=sshpass,
                        port = sshport,
                        missing_host_key=spur.ssh.MissingHostKey.accept)
                        
        #### START prepares ssh commands to run                        


        #### END prepares ssh commands to run

        # logs in to host, runs commands, outputs results to new window
        #with shell:
            #result = shell.run(["uptime"])
            #return(result.output)        
        return render_template('customcommand_results.html')
                        
    return render_template('customcommand.html',
        title='Custom Command')

