# fsnd-logs-analysis

This project is part of the Full Stack Nanodegree program being offered by Udacity in partnership with Google, AWS, Github & AT&T.  The high level overview of this project is to showcase integration of Postgres drivers,
handling SQL calls, formatting and manipulating records, and more.  While simple in nature, it showcases how effective Python can be at implementing design patterns that prefer re-usability.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Install Virtual Box
VirtualBox is software that runs virtual machines. Download it from [virtualbox.org](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for Windows. No need to download the extension pack or the SDK.

### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for Windows.

### Download the VM configuration
1. Download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).
2. Move the directory FSND-Virtual-Machine to a directory of your choosing if you want.
3. Download the [Vagrant file configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2019/March/5c7ebe7a_vagrant-configuration-windows/vagrant-configuration-windows.zip) to replace the current Vagrant file.

### Download the data
Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will unzip this file and put the file "newsdata.sql" into the "vagrant" directory.

### Start the virtual machine
1. Run Git bash in the 'vagrant' directory or cd into it.
2. From your terminal, run the command:
```
vagrant up
```
3. When the above is finished running, run the command:
```
vagrant ssh
```
4. If your shell prompt starts with the word "vagrant", you're logged into your Linux VM.

### Load the data
In your terminal, created in the instructions above, run the following:
```
psql -d news -f newsdata.sql
```
 ### Run LogsAnalysis.py
 With the data loaded, download "LogsAnalysis.py" from my repo and put it in the "vagrant" directory. Run the following command:
 ```
 python LogsAnalysis.py
 ```
 or, if the above doesn't work
 ```
 python3 LogsAnalysis.py
 ```
 Compare the "LogsAnalysis.txt" in my repo to the one created in your "vagrant" directory".
 
 ### Exit Vagrant
 Run the following command to exit vagrant,
 ```
 exit
 ```

End with an example of getting some data out of the system or using it for a little demo

## Deployment

To date, this is only intended to be ran locally; whether that be bare-metal, a contrainer, VM, etc.

## Built With

* [Python 3](https://docs.python.org/3/) - The web framework used
* [Psycopg2](http://initd.org/psycopg/docs/) - Dependency Management

## Authors

* **Cory A. Ramirez** - *Initial work* - [Cory A. Ramirez](https://github.com/CoryARamirez)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks Udacity!
* Fore more about me, view [Pending Website](www.google.com)
