#! /usr/bin/expect -f

set timeout -1

spawn ssh student@172.27.26.188

expect "*: "
send "cs641\r"
expect "*: "
send "the_cryptonics\r"
expect "*: "
send "bkb\r"
expect "*: "
send "5\r"
expect "*> "
send "go\r"
expect "*> "
send "wave\r"
expect "*> "
send "dive\r"
expect "*> "
send "go\r"
expect "*> "
send "read\r"

set fin_name "inputs.txt"
set fin [open "$fin_name" r]
set in_data [read $fin]

set fout_name "output.txt"
set fout [open $fout_name "w"]
 
# Read line by line
foreach line $in_data {
  # puts "$line\r"
  
  expect "> "
  send "$line\r"

  expect "$line\r"  # discard command echo
  expect "Slowly, a new text starts appearing on the screen. It reads ..."
  expect "\n\t*\n"  # match and save the result
  puts -nonewline $fout "$expect_out(0,string)"

  expect "Press c to continue> "
  send "c\r"
}
close $fin
close $fout


expect "*> "
send "back\r"
expect "*> "
send "exit\r"