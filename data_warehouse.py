import pandas as pd
import numpy as np

def get_inventory_data():
    np.random.seed(42)
    return pd.DataFrame({
        "SKU_ID": [f"SKU-{1000+i}" for i in range(50)],
        "Item_Name": [f"Component-{chr(65 + (i % 26))}" for i in range(50)],
        "Unit_Cost_USD": np.round(np.random.uniform(5, 500, size=50), 2),
        "Annual_Qty_Sold": np.random.randint(100, 5000, size=50),
        "Current_Stock_Level": np.random.randint(10, 800, size=50),
        "Lead_Time_Days": np.random.randint(3, 45, size=50)
    })

def get_carrier_data():
    np.random.seed(43)
    carriers = ["FedEx", "UPS", "DHL", "J.B. Hunt", "Schneider"]
    reasons = ["On-Time", "Weather Delay", "Customs Hold", "Traffic Bottleneck", "Mechanical Failure"]
    return pd.DataFrame({
        "Tracking_Number": [f"TRK{np.random.randint(100000, 999999)}" for _ in range(40)],
        "Carrier_Name": np.random.choice(carriers, size=40),
        "Origin_Hub": np.random.choice(["LAX", "ORD", "JFK", "DFW"], size=40),
        "SLA_Delivery_Days": np.random.choice([2, 3, 5, 7], size=40),
        "Actual_Delivery_Days": np.random.randint(1, 8, size=40),
        "Delay_Reason": np.random.choice(reasons, size=40, p=[0.7, 0.1, 0.05, 0.1, 0.05])
    })

def get_procurement_data():
    np.random.seed(44)
    countries = ["USA", "Germany", "China", "Mexico", "Vietnam"]
    return pd.DataFrame({
        "PO_Number": [f"PO-{5000+i}" for i in range(30)],
        "Supplier_ID": [f"SUP-{100+np.random.randint(1,10)}" for _ in range(30)],
        "Supplier_Country": np.random.choice(countries, size=30),
        "Order_Qty": np.random.randint(500, 10000, size=30),
        "Defect_Qty": np.random.randint(0, 150, size=30),
        "Unit_Price_USD": np.round(np.random.uniform(1.5, 45.0, size=30), 2)
    })

def get_lastmile_data():
    np.random.seed(45)
    return pd.DataFrame({
        "Trip_ID": [f"TRIP-{7000+i}" for i in range(35)],
        "Vehicle_Type": np.random.choice(["Van", "Box Truck", "Electric Runner"], size=35),
        "Route_Distance_KM": np.round(np.random.uniform(5, 120, size=35), 1),
        "Fuel_Consumed_Liters": np.round(np.random.uniform(2, 40, size=35), 1),
        "Stops_Completed": np.random.randint(5, 30, size=35),
        "Customer_Rating": np.round(np.random.uniform(3.5, 5.0, size=35), 1)
    })

def get_freight_audit_data():
    np.random.seed(46)
    base = np.random.randint(800, 3500, size=30)
    billed = base + np.random.randint(-150, 600, size=30)
    return pd.DataFrame({
        "Invoice_ID": [f"INV-{9000+i}" for i in range(30)],
        "Load_ID": [f"LD-{2000+i}" for i in range(30)],
        "Base_Rate": base,
        "Fuel_Surcharge": np.round(base * np.random.uniform(0.12, 0.22, size=30), 2),
        "Estimated_Cost": base + (base * 0.15),
        "Billed_Cost": billed
    })

def get_manufacturing_data():
    np.random.seed(47)
    return pd.DataFrame({
        "Shift_ID": np.random.choice(["Morning", "Evening", "Night"], size=40),
        "Machine_ID": [f"LINE-0{np.random.randint(1,5)}" for _ in range(40)],
        "Planned_Run_Time_Min": [480 for _ in range(40)],
        "Actual_Run_Time_Min": 480 - np.random.choice([0, 15, 30, 60], size=40, p=[0.6, 0.2, 0.1, 0.1]),
        "Target_Units": np.random.randint(1000, 1500, size=40),
        "Produced_Units": np.random.randint(800, 1490, size=40)
    })

def get_returns_data():
    np.random.seed(48)
    reasons = ["Defective Item", "Wrong Size Ordered", "Buyer Remorse", "Damaged in Transit"]
    return pd.DataFrame({
        "Return_ID": [f"RET-{3000+i}" for i in range(30)],
        "SKU_ID": [f"SKU-{1000+np.random.randint(0,20)}" for _ in range(30)],
        "Return_Reason": np.random.choice(reasons, size=30),
        "Item_Condition": np.random.choice(["Refurbished-Ready", "Scrap/Liquidate", "Return to Vendor"], size=30),
        "Refund_Amount_USD": np.round(np.random.uniform(20, 800, size=30), 2),
        "Processing_Time_Days": np.random.randint(1, 14, size=30)
    })

def get_crossdock_data():
    np.random.seed(49)
    return pd.DataFrame({
        "Trailer_ID": [f"TRLR-{4000+i}" for i in range(30)],
        "Inbound_Carrier": np.random.choice(["Swift", "Knight", "Werner"], size=30),
        "Dock_Door_Assigned": np.random.randint(1, 18, size=30),
        "Unload_Duration_Min": np.random.randint(20, 110, size=30),
        "Dwell_Time_Hours": np.round(np.random.uniform(0.5, 6.0, size=30), 1)
    })

def get_omnichannel_data():
    np.random.seed(50)
    return pd.DataFrame({
        "Order_ID": [f"ORD-{8000+i}" for i in range(50)],
        "Pick_Time_Sec": np.random.randint(30, 400, size=50),
        "Pack_Time_Sec": np.random.randint(20, 180, size=50),
        "Courier_Manifest_Sec": np.random.randint(10, 90, size=50),
        "Fulfillment_Zone": np.random.choice(["Zone-A", "Zone-B", "Zone-C"], size=50),
        "Error_Flag": np.random.choice([0, 1], size=50, p=[0.94, 0.06])
    })
