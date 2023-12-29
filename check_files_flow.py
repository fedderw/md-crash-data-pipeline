import os
import pandas as pd
from prefect import task, flow

# Task to check if all expected columns are present in a file
@task
def check_columns(file_path, expected_columns):
    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")
    df = pd.read_csv(file_path)
    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns in {file_path}: {missing_columns}")

# Flow to check files for expected columns
@flow(name="Check Files Flow")
def check_files_flow():
    files_to_check = {
        "data/raw/CrashMap_CIRCUMSTANCES_data.csv": ["Reportnumber", "CircumstancesCode", "CircumstancesPersonID", "CircumstancesType", "CircumstancesVehicleID"],
        "data/raw/CrashMap_DRIVER_data.csv": ["Reportnumber", "DriverID", "DriverAirbagDeployed", "DriverAlcoholTestIndicator", "DriverAlcoholTestType", "DriverBAC", "DriverCondition", "Driverdistractedby", "DriverDOB", "DriverDrugTestIndicator", "DriverDrugTestResult", "DriverEjection", "DriverEquipmentProblem", "DriverHasCDL", "DriverInjurySeverity", "DriverSafetyEquipment", "DriverSex", "DriverSubstanceUse", "DriverVehicleID"],
        "data/raw/CrashMap_NONMOTORIST_data.csv": ["Reportnumber", "NonMotoristID", "NonMotoristActions", "NonMotoristAlcoholTestindicator", "NonMotoristAlcoholTestType", "NonMotoristBAC", "NonMotoristCondition", "NonMotoristDOB", "NonMotoristDrugTestIndicator", "NonMotoristDrugTestResult", "NonMotoristInjurySeverity", "NonMotoristLocation", "NonMotoristMovement", "NonMotoristObeyTrafficSignal", "NonMotoristSafetyEquipment", "NonMotoristSex", "NonMotoristSubstanceUse", "NonMotoristType", "NonMotoristUnitNumberFirstStrike", "NonMotoristVisibility"],
        "data/raw/CrashMap_PASSENGER_data.csv": ["Reportnumber", "PassengerID", "PassengerAirbagDeployed", "PassengerDOB", "PassengerEjection", "PassengerEquipmentProblem", "PassengerInjurySeverity", "PassengerSafetyEquipment", "PassengerSeat", "PassengerSeatingLocation", "PassengerSeatingRow", "PassengerSex", "PassengerVehicleID"],
        "data/raw/CrashMap_REPORT_data.csv": ["AgencyCode", "Reportnumber", "CountyOfCrash", "Reporttype", "UseData", "Crashdate", "CrashPoint", "Latitude", "Longitude", "Collisiontype", "Fixedobjectstruck", "Harmfuleventone", "Harmfuleventtwo", "Interchangearea", "Intersectiontype", "Junction", "Lanedirection", "Lanenumber", "Lanetype", "Lighting", "Logmile Dir", "MaintenanceClosure", "MaintenanceLocation", "MaintenanceWorkersPresent", "MaintenanceZone", "Milepoint", "Milepointdirection", "Milepointdistance", "Milepointdistanceunits", "Nontraffic", "Numberoflanes", "Offroaddescription", "Reference Roadname", "Reference Route Number", "Reference Route Type", "Road Name", "Roadalignment", "Roadcondition", "Roaddivision", "Roadgrade", "Route Number", "Route Type", "Schoolbusinvolvement", "Status Id", "Surfacecondition", "Timeofcrash", "Trafficcontrol", "Trafficcontrolfunctioning", "Weather", "Doctype"],
        "data/raw/CrashMap_VEHICLE_data.csv": ["Reportnumber", "Vehicleid", "CommercialBodyType", "CommercialCarrierClassification", "CommercialConfiguration", "CommercialGVW", "CommercialHazmatClass", "CommercialHazmatNumber", "CommercialHazmatPlacardVisible", "CommercialHazmatSpill", "CommercialNumberofaxles", "Continuedirection", "Damageextent", "Driverlessvehicle", "Emergencymotorvehicleuse", "Fire", "Firstimpact", "Goingdirection", "Mainimpact", "Mostharmfulevent", "Parkedvehicle", "Speedlimit", "Towedunittype", "Unitnumber", "Vehiclebodytype", "VehicleBusUse", "VehicleLeftScene", "Vehiclemake", "Vehiclemodel", "Vehiclemovement", "VehicleSpecialFunction", "Vehicleyear", "VIN"]
    }

    for file_path, expected_cols in files_to_check.items():
        check_columns(file_path, expected_cols)

# Run the flow
if __name__ == "__main__":
    check_files_flow()
