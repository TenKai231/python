import re     # Import modul regex
import argparse



# pola= '^a...s$'
# string_tes= 'abyss'
# hasil= re.match(pola, string_tes)
 
# if hasil:
#     print("Pencarian berhasil.")
# else:
#     print("Pencarian gagal.") 


parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help='Nama pengguna')
parser.add_argument('-t', '--tanggal_lahir', required=True, help='Tanggal lahir pengguna')
args = parser.parse_args()

print("Hallo ini sapa dari pembuat python, " + args.nama + ",!" + args.tanggal_lahir)