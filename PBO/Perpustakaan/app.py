from books.book import book
from members.member import member
from transactions.transactions import transaction

book = book("python programming", "Reg A - PBO")
member = member("Acha Qilal Addinutama","M0017")
transaction = transaction(book, member, "2024-03-02")

print(f"peminjaman buku \ntanggal peminjaman: {transaction.date}")
print(f"ID member: {transaction.member.member_id}\nnama member: {transaction.member.name}")
print(f"\nbuku \njudul buku: {transaction.book.title}\nauthor: {transaction.book.author}")