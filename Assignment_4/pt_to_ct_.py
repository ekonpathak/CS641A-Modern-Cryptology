import pexpect

child = pexpect.spawn('/usr/bin/ssh student@172.27.26.188')
child.expect('student@172.27.26.188\'s password:')
child.sendline('cs641')
child.expect('Enter your group name: ', timeout=1) 
child.sendline("the_cryptonics")

child.expect('Enter password: ', timeout=1)
child.sendline("bkb")

child.expect('\r\n\r\n\r\nYou have solved 4 levels so far.\r\nLevel you want to start at: ', timeout=1)
# Note: After clearing level 3 this needs to be changed to "solved 4 levels so far"
child.sendline("4")	

# child.expect('\r\nThe rumbling sound is very loud here. It is coming from \r\n your right side. A cold blast of air hits you sending \r\n shivers up your spine. You look in that direction. \r\n There is a large opening on the right from where the \r\n\tsound and the air is coming from. There is a fair amount\r\n\tof light also coming from that direction (you realize that\r\n\tyou have not lighted a matchstick and still you can see).\r\n\tThere is another door, with a panel nearby, to your left \r\n\twhich is closed. The chamber is rocky and cold. Another \r\n\tblast of air hits you from your right and you shiver again. \r\n\r\n> ', timeout=120)
# child.sendline("read")

# child.expect('.*')

# child.expect('.*')
# child.sendline("go")

# child.expect('.*')
# child.sendline("dive")

# child.expect('.*')
# child.sendline("dive")

# child.expect('.*')
# child.sendline("back")

# child.expect('.*')
# child.sendline("pull")

# child.expect('.*')
# child.sendline("enter")

# child.expect('.*')
# child.sendline("jump")

# child.expect('.*')
# child.sendline("jump")

# child.expect('.*')
# child.sendline("back")

# child.expect('.*')
# child.sendline("pull")

# child.expect('.*')
# child.sendline("back")

# child.expect('.*')
# child.sendline("back")

# child.expect('.*')
# child.sendline("enter")

# child.expect('.*')
# child.sendline("wave")

# child.expect('.*')
# child.sendline("back")


# child.expect('.*')
# child.sendline("back")

# child.expect('.*')
# child.sendline("thrnxxtzy")

# child.expect('.*')
# child.sendline("read")

# child.expect('.*')
# child.sendline("the_magic_of_wand")

# child.expect('.*')
# child.sendline("c")

child.expect('.*')
child.sendline("read")


f = open("plaintext_set2.txt", 'r')
f1= open("ciphertext_set2.txt",'w')

for line in f.readlines():
	child.sendline(line)
	print(child.before)
	f1.writelines(str(child.before)[48:64]+"\n")
	child.expect("Slowly, a new text starts*")
	child.sendline("c")
	child.expect('The text in the screen vanishes!')

data = child.read()
print(data)
child.close()
print(child.before, child.after)

f.close()
f1.close()