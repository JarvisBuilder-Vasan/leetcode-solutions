class Solution:
    def dayOfYear(self, date: str) -> int:
        parts=date.split("-")
        year=int(parts[0])
        month=int(parts[1])
        day=int(parts[2])

        days=[31,28,31,30,31,30,31,31,30,31,30,31]

        total=sum(days[:month-1])
        total+=day
        if (year%400==0) or (year%4==0 and year%100!=0):
            if month>2:
                total+=1

        return total
