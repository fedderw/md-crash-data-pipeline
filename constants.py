# Combined dictionary for all CSV mappings
column_mappings = {
    "circumstances": {
        "Reportnumber": "report_number",
        "CircumstancesCode": "circumstances_code",
        "CircumstancesPersonID": "circumstances_person_id",
        "CircumstancesType": "circumstances_type",
        "CircumstancesVehicleID": "circumstances_vehicle_id"
    },
    "driver": {
        "Reportnumber": "report_number",
        "DriverID": "driver_id",
        "DriverAirbagDeployed": "driver_airbag_deployed",
        "DriverAlcoholTestIndicator": "driver_alcohol_test_indicator",
        "DriverAlcoholTestType": "driver_alcohol_test_type",
        "DriverBAC": "driver_bac",
        "DriverCondition": "driver_condition",
        "Driverdistractedby": "driver_distracted_by",
        "DriverDOB": "driver_dob",
        "DriverDrugTestIndicator": "driver_drug_test_indicator",
        "DriverDrugTestResult": "driver_drug_test_result",
        "DriverEjection": "driver_ejection",
        "DriverEquipmentProblem": "driver_equipment_problem",
        "DriverHasCDL": "driver_has_cdl",
        "DriverInjurySeverity": "driver_injury_severity",
        "DriverSafetyEquipment": "driver_safety_equipment",
        "DriverSex": "driver_sex",
        "DriverSubstanceUse": "driver_substance_use",
        "DriverVehicleID": "driver_vehicle_id"
    },
    "nonmotorist": {
        "Reportnumber": "report_number",
        "NonMotoristID": "non_motorist_id",
        "NonMotoristActions": "non_motorist_actions",
        "NonMotoristAlcoholTestindicator": "non_motorist_alcohol_test_indicator",
        "NonMotoristAlcoholTestType": "non_motorist_alcohol_test_type",
        "NonMotoristBAC": "non_motorist_bac",
        "NonMotoristCondition": "non_motorist_condition",
        "NonMotoristDOB": "non_motorist_dob",
        "NonMotoristDrugTestIndicator": "non_motorist_drug_test_indicator",
        "NonMotoristDrugTestResult": "non_motorist_drug_test_result",
        "NonMotoristInjurySeverity": "non_motorist_injury_severity",
        "NonMotoristLocation": "non_motorist_location",
        "NonMotoristMovement": "non_motorist_movement",
        "NonMotoristObeyTrafficSignal": "non_motorist_obey_traffic_signal",
        "NonMotoristSafetyEquipment": "non_motorist_safety_equipment",
        "NonMotoristSex": "non_motorist_sex",
        "NonMotoristSubstanceUse": "non_motorist_substance_use",
        "NonMotoristType": "non_motorist_type",
        "NonMotoristUnitNumberFirstStrike": "non_motorist_unit_number_first_strike",
        "NonMotoristVisibility": "non_motorist_visibility"
    },
    "passenger": {
        "Reportnumber": "report_number",
        "PassengerID": "passenger_id",
        "PassengerAirbagDeployed": "passenger_airbag_deployed",
        "PassengerDOB": "passenger_dob",
        "PassengerEjection": "passenger_ejection",
        "PassengerEquipmentProblem": "passenger_equipment_problem",
        "PassengerInjurySeverity": "passenger_injury_severity",
        "PassengerSafetyEquipment": "passenger_safety_equipment",
        "PassengerSeat": "passenger_seat",
        "PassengerSeatingLocation": "passenger_seating_location",
        "PassengerSeatingRow": "passenger_seating_row",
        "PassengerSex": "passenger_sex",
        "PassengerVehicleID": "passenger_vehicle_id"
    },
    "report":{
        "AgencyCode": "agency_code",
        "Reportnumber": "report_number",
        "CountyOfCrash": "county_of_crash",
        "Reporttype": "report_type",
        "UseData": "use_data",
        "Crashdate": "crash_date",
        "CrashPoint": "crash_point",
        "Latitude": "latitude",
        "Longitude": "longitude",
        "Collisiontype": "collision_type",
        "Fixedobjectstruck": "fixed_object_struck",
        "Harmfuleventone": "harmful_event_one",
        "Harmfuleventtwo": "harmful_event_two",
        "Interchangearea": "interchange_area",
        "Intersectiontype": "intersection_type",
        "Junction": "junction",
        "Lanedirection": "lane_direction",
        "Lanenumber": "lane_number",
        "Lanetype": "lane_type",
        "Lighting": "lighting",
        "LogmileDir": "logmile_dir",
        "MaintenanceClosure": "maintenance_closure",
        "MaintenanceLocation": "maintenance_location",
        "MaintenanceWorkersPresent": "maintenance_workers_present",
        "MaintenanceZone": "maintenance_zone",
        "Milepoint": "milepoint",
        "Milepointdirection": "milepoint_direction",
        "Milepointdistance": "milepoint_distance",
        "Milepointdistanceunits": "milepoint_distance_units",
        "Nontraffic": "non_traffic",
        "Numberoflanes": "number_of_lanes",
        "Offroaddescription": "offroad_description",
        "ReferenceRoadname": "reference_road_name",
        "ReferenceRouteNumber": "reference_route_number",
        "ReferenceRouteType": "reference_route_type",
        "RoadName": "road_name",
        "Roadalignment": "road_alignment",
        "Roadcondition": "road_condition",
        "Roaddivision": "road_division",
        "Roadgrade": "road_grade",
        "RouteNumber": "route_number",
        "RouteType": "route_type",
        "Schoolbusinvolvement": "school_bus_involvement",
        "StatusId": "status_id",
        "Surfacecondition": "surface_condition",
        "Timeofcrash": "time_of_crash",
        "Trafficcontrol": "traffic_control",
        "Trafficcontrolfunctioning": "traffic_control_functioning",
        "Weather": "weather",
        "Doctype": "doctype"
    },
    "vehicle": {
        "Reportnumber": "report_number",
        "Vehicleid": "vehicle_id",
        "CommercialBodyType": "commercial_body_type",
        "CommercialCarrierClassification": "commercial_carrier_classification",
        "CommercialConfiguration": "commercial_configuration",
        "CommercialGVW": "commercial_gvw",
        "CommercialHazmatClass": "commercial_hazmat_class",
        "CommercialHazmatNumber": "commercial_hazmat_number",
        "CommercialHazmatPlacardVisible": "commercial_hazmat_placard_visible",
        "CommercialHazmatSpill": "commercial_hazmat_spill",
        "CommercialNumberofaxles": "commercial_number_of_axles",
        "Continuedirection": "continue_direction",
        "Damageextent": "damage_extent",
        "Driverlessvehicle": "driverless_vehicle",
        "Emergencymotorvehicleuse": "emergency_motor_vehicle_use",
        "Fire": "fire",
        "Firstimpact": "first_impact",
        "Goingdirection": "going_direction",
        "Mainimpact": "main_impact",
        "Mostharmfulevent": "most_harmful_event",
        "Parkedvehicle": "parked_vehicle",
        "Speedlimit": "speed_limit",
        "Towedunittype": "towed_unit_type",
        "Unitnumber": "unit_number",
        "Vehiclebodytype": "vehicle_body_type",
        "VehicleBusUse": "vehicle_bus_use",
        "VehicleLeftScene": "vehicle_left_scene",
        "Vehiclemake": "vehicle_make",
        "Vehiclemodel": "vehicle_model",
        "Vehiclemovement": "vehicle_movement",
        "VehicleSpecialFunction": "vehicle_special_function",
        "Vehicleyear": "vehicle_year",
        "VIN": "vin"
    }
}