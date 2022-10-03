class NodeTabungan:

    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rek, nama, saldo=0):
        self.no_rekening = no_rek
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def hapus(self, idx):
        p = self.head

        if idx == 0:
            self.head = p.next
            del p
            self.size -= 1
        
        elif idx == self.size-1:
            while p.next != self.tail:
                p = p.next

            del self.tail
            self.tail = p
            self.tail.next = None
            self.size -= 1

        else:
            for i in range(idx-1):
                p = p.next

            p.next = p.next.next
            del p.next
        self.size -= 1

    def cetak(self):
        p = self.head

        while p:
            print("Norek : {}" .format(p.no_rekening))
            print("Nama  : {}" .format(p.nama))
            print("Saldo : {}" .format(p.saldo))
            print()

            p = p.next
    
    def insert_head(self, norek, nama, saldo):
        new = NodeTabungan(norek, nama, saldo)

        if self.size == 0:
            self.head = new
            self.tail = new

        else:
           new.next = self.head
           self.head = new 

        self.size += 1
    
    def filter(self, x):
        p = self.head
        idx = 0
        self.hitung = 0

        while p:
            if p.saldo < x:
                self.hapus(idx)
                self.hitung += 1
            idx += 1
        print("Rekening yang berhasil di hapus sebanyak : {} buah" .format(self.hitung))

    def update(self, bunga):
        p = self.head

        if bunga >= 0 and bunga <= 100:
            while p:
                p.saldo = p.saldo + (p.saldo*bunga)
            print("semua saldo rekening berhasil ditambah sebanyak {}%" .format(bunga))
        
        else:
            print("maaf besaran harus diantara 0 - 100")

slnc = SLNC()   

if __name__ == "__main__":

    slnc.insert_head(201,"Hanif", 250000)
    slnc.insert_head(110, "Yudha", 150000)
    slnc.cetak()
    slnc.filter(100)
    slnc.print()
    slnc()