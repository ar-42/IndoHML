import os, sys, time

os.system("clear")
time.sleep(2)
print ("\033[1;32mSilahkan Masukkan Username & Password Script IndoHML")

print ("\033[1;32mBagi yang tidak tahu silahkan akses https://indoxploit.id")
print ("")
print ("")

time.sleep(1)


username = 'Indo'
password = 'Xploit'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:
                        print ""
                        print ""
                        time.sleep(1)
			print "\033[1;32mLogin Sukses!", 

			os.system("bash run.sh")
                        sys.exit()



		else:

                        time.sleep(1)
                        print ""
                        print ""
			print "\033[1;32mMaaf Password Salah...\033[00m"
                        time.sleep(1)
                        print ""
			print "\033[1;32mCoba ambil Password di halaman berikut..\n"
                        time.sleep(3)
			restart()



	else:

                time.sleep(1)
                print ""
                print ""
		print "\033[1;32mUSERNAME SALAH.\033[00m"
                time.sleep(1)
                print ""
		print "Coba ketik Indo\n"
                time.sleep(2)
                os.system("clear")

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
