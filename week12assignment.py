data = """Hammer,ZoneA,100,50
Drill,ZoneB,20,10
Saw,ZoneA,30,15
Nails,ZoneC,200,300
Screws,ZoneB,10,10
Corrupt,Line,Error
Paint,ZoneC,40,5
"""
with open('warehouse_stock.txt', 'w') as f:
    f.write(data)

def audit_inventory(filename):
    with open ('warehouse_stock.txt', 'r') as filename:
        zone_totals = {}
        low_stock_items = []
        for line in filename:
            try:
                Product,Zone,ShelfQty,BackroomQty = line.split(',')
                TotalStock = int(ShelfQty) + int(BackroomQty)
                if Zone in zone_totals:
                    zone_totals[Zone] += TotalStock
                else:
                    zone_totals[Zone] = TotalStock
                if TotalStock < 50:
                    low_stock_items.append((Product, TotalStock))
            except ValueError:
                continue
        return zone_totals,low_stock_items
def generate_reorder_list(zone_totals, low_stock_items):
    with open('inventory_report.txt', 'w') as file:
        file.write('ZONE INVENTORY COUNTS\n')
        file.write('---------------------\n')
        for zone,total in zone_totals.items():
            file.write(f'{zone}: {total}\n')
        file.write(f'REORDER ALERTS (< 50 items)\n')
        file.write(f'---------------------------\n')
        for product,total in low_stock_items:
            file.write(f'{product} ({total} items)\n')
zone_totals,low_stock_items =audit_inventory('warehouse_stock.txt')
generate_reorder_list(zone_totals, low_stock_items)
