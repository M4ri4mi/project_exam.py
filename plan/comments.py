# პროექტი იქნება კალკულატორის დასატესტად, რომელიც მოიცავს ათ კითხვიან გამოცდასაც
# რადგან მთლიანად კოდი ჯერ არ დამიმთავრებია, აქ ავტვირთავ მხოლოდ კალკულატორის კოდს
# დიზაინს ასევე დავამტავრებ ხუთშაბათისტვის, დანარჩენ კოდთან ერთად

# გამოცდაში json file-ით შემოვიყვან ათ მარტივ კითხვას, მაგალითად 85+15
# პროგრამა იქყება შემდეგნაირად:
# start an exam, აქ დაჭერისას ჩაიტვირთება პირველი კითხვა (20*6 =?), 
# ქვემოთ ორი არჩევანით: answer the question; ან use calculator
# use calculator-ზე დაჭერისას იხსნება ჩვეულებრივი კალკულატორი, +-/* ფუნქციებით
# კალკულატორს ასევე აქვს reset და delete (ბოლო ციფრის წაშლა), ასევე return ფუნქცია
# return ფუნქციით გავდივართ უკან, კითხვის გვერდზე
# მეორე option არის answer the question, სწორი პასუხისას გვიწერს correct, არასწორისას incorrect
# შემდეგ გადავდივართ მეორე კითხვაზე და ასე შემდეგ
# ბოლო კითხვაზე პასუხის გაცემისას, თუ სწორად გავეციტ პოასუხი 5-ზე მეტ კიტხვას, გვიწწერ ცააბარე
# 5ზე ნაკლები სწორი პასუხისას მონაწილე იჭრება გამოცდაში