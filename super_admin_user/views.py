from .models import SuperAdmin, AdminUserList
from django.shortcuts import render, redirect
from .templates.super_admin_user.admin.adminForm import AdminUserForm
from django.contrib import messages
from django.db import connection
from .models import MastersList
from admin_user.forms.adminRoleForm import AdminUserRoleForm


def login(request):
    return render(request, 'super_admin_user/login.html')


def login_auth(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # SuperAdmin.objects.
            try:
                user = SuperAdmin.objects.get( username=username, password=password)
                if user is not None:
                    print(user.name)
                    
                    return render(request, 'super_admin_user/dashboard.html',{'user':user})
                else:
                    messages.error(request, 'Invalid username or password')
                    return render(request, 'super_admin_user/login.html')
            except Exception as e:
                print(e)
                return render(request, 'super_admin_user/login.html')
    except Exception as e:
         print(e)


def dashboard(request):
    return render(request, 'super_admin_user/dashboard.html')


def logout_root(request):
    return redirect('login_root')

# views.py

def createTable(tableName,t,org):
    try:
     with connection.cursor() as cursor:
        if(t=="state"):
            sql=f'''SET FOREIGN_KEY_CHECKS=0;
            CREATE TABLE IF NOT EXISTS {tableName} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        state VARCHAR(255) NOT NULL UNIQUE,
        state_code VARCHAR(2) NOT NULL UNIQUE,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );SET FOREIGN_KEY_CHECKS=1;
        '''
            cursor.execute(sql)
        elif (t == "city"):
            sql = f'''SET FOREIGN_KEY_CHECKS=0;
            CREATE TABLE IF NOT EXISTS {tableName} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city_name VARCHAR(255) NOT NULL UNIQUE,
                state_id INT,
                FOREIGN KEY (state_id) REFERENCES {org}_state_master(id),
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            );SET FOREIGN_KEY_CHECKS=1;
            '''
            cursor.execute(sql)

        elif (t == "ground"):
            sql = f'''SET FOREIGN_KEY_CHECKS=0;
            CREATE TABLE IF NOT EXISTS {tableName} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            org_id VARCHAR(255),
            google_location TEXT,
            year_of_construction VARCHAR(255),
            phone_numbers VARCHAR(255),
            slop_ratio VARCHAR(255),
            ground_name VARCHAR(255),
            state_code VARCHAR(2),
            state_name VARCHAR(255),
            city_name VARCHAR(255),
            count_main_pitches INT,
            count_practice_pitches INT,
            is_side_screen BOOLEAN,
            count_placement_side_screen INT,
            is_broadcasting_facility BOOLEAN,
            is_irrigation_pitches BOOLEAN,
            count_hydrants INT,
            count_pumps INT,
            count_showers INT,
            is_lawn_nursary BOOLEAN,
            name_centre_square VARCHAR(255),
            is_curator_room BOOLEAN,
            is_seperate_practice_area BOOLEAN,
            outfield VARCHAR(255),
            profile_of_outfield VARCHAR(255),
            lawn_species VARCHAR(255),
            is_drainage_system_available BOOLEAN,
            is_water_drainage_system BOOLEAN,
            is_irrigation_system_available BOOLEAN,
            is_availability_of_water BOOLEAN,
            water_source text,
            storage_capacity_in_litres INT,
            count_pop_ups INT,
            size_of_pumps VARCHAR(255),
            is_automation_if_any BOOLEAN,
            is_ground_equipments BOOLEAN,
            is_maintenance_contract BOOLEAN,
            is_maintenance_agency BOOLEAN,
            boundary_size_mtrs text,
            is_availability_of_mot BOOLEAN,
            is_machine_shed BOOLEAN,
            is_soil_shed BOOLEAN,
            is_pitch_or_run_up_covers BOOLEAN,
            size_of_covers_in_mtrs VARCHAR(255),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );SET FOREIGN_KEY_CHECKS=1;
            '''
            cursor.execute(sql)
        elif (t == "pitch"):
            sql = f'''SET FOREIGN_KEY_CHECKS=0;
            CREATE TABLE IF NOT EXISTS {tableName} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            org_id VARCHAR(255),
            ground_id INT,
            size_pitch_square text,
            pitch_no VARCHAR(255),
            pitch_type VARCHAR(255),
            profile_of_pitches VARCHAR(255),
            last_used_date DATE,
            last_used_match VARCHAR(255),
            soil_type VARCHAR(255),
            is_uniformtiy_of_grass BOOLEAN,
            size_of_grass text,
            mowing_last_date DATE,
            size_pitch VARCHAR(45),
            pitch_placement VARCHAR(45),
            pitch_in_out VARCHAR(45),
            mowing_size text,
            start_date_of_pitch_preparation DATE,
            date_pitch_construction DATE,
            pitch_details text,
            FOREIGN KEY (ground_id) REFERENCES {org}_ground_master(id),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );SET FOREIGN_KEY_CHECKS=1;
            '''
            cursor.execute(sql)
            
        elif (t == "curator_daily_recording"):
            cursor.execute(f'''SET FOREIGN_KEY_CHECKS=0;

CREATE TABLE IF NOT EXISTS {tableName} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pitch_id INT,
    pitch_location VARCHAR(100),
    rolling_start_date VARCHAR(50),
    min_temp VARCHAR(45),
    max_temp VARCHAR(45),
    forecast TEXT,
    clagg_hammer TEXT,
    moisture TEXT,

    machinery_id VARCHAR(100),
    no_of_passes VARCHAR(50),
    rolling_speed VARCHAR(50),
    last_watering_on VARCHAR(50),
    quantity_of_water VARCHAR(50),
    time_of_application VARCHAR(20),
    time_roller VARCHAR(20),
   

    mover_machinery_id VARCHAR(100),
    date_mowing_done_last VARCHAR(50),
    time_of_application_mover VARCHAR(20),
    mowing_done_at_mm VARCHAR(50),

    is_fertilizers_used VARCHAR(20),
    fertilizers_details TEXT,
    chemical_details_remark LONGTEXT,
    remark_by_groundsman TEXT,

    out_machinery_id VARCHAR(100),
    out_no_of_passes VARCHAR(50),
    out_rolling_speed VARCHAR(50),
    out_last_watering_on VARCHAR(50),
    out_quantity_of_water VARCHAR(50),
    out_time_of_application VARCHAR(20),
    out_time_roller VARCHAR(20),

    out_mover_machinery_id VARCHAR(100),
    out_date_mowing_done_last VARCHAR(50),
    time_of_application_out_mover VARCHAR(20),
    out_mowing_done_at_mm VARCHAR(50),
    out_is_fertilizers_used VARCHAR(20),
    out_fertilizers_details TEXT,
    out_chemical_details_remark LONGTEXT,
    out_remark_by_groundsman TEXT,

    practice_machinery_id VARCHAR(100),
    practice_no_of_passes VARCHAR(50),
    practice_rolling_speed VARCHAR(50),
    practice_last_watering_on VARCHAR(50),
    practice_quantity_of_water VARCHAR(50),
    practice_time_of_application VARCHAR(20),
    practice_time_roller VARCHAR(20),

    practice_mover_machinery_id VARCHAR(100),
    practice_date_mowing_done_last VARCHAR(50),
    time_of_application_practice_mover VARCHAR(20),
    practice_mowing_done_at_mm VARCHAR(50),
    practice_is_fertilizers_used VARCHAR(20),
    practice_fertilizers_details TEXT,
    practice_chemical_details_remark LONGTEXT,
    practice_remark_by_groundsman TEXT,

    time_of_application_chemical VARCHAR(20),
    out_time_of_application_chemical VARCHAR(20),
    practice_time_of_application_chemical VARCHAR(20),

    recording_type VARCHAR(45),
    ground_id INT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    pitch_main VARCHAR(20),
    pitch_practice VARCHAR(20),
    outfield VARCHAR(20),
    practice_area VARCHAR(20),
    
    pitch_main_chemical_weight VARCHAR(20),
    pitch_practice_chemical_weight VARCHAR(20),
    outfield_chemical_weight VARCHAR(20),
    practice_area_chemical_weight VARCHAR(20),
    
    pitch_main_chemical_unit VARCHAR(20),
    pitch_practice_chemical_unit VARCHAR(20),
    outfield_chemical_unit VARCHAR(20),
    practice_area_chemical_unit VARCHAR(20),
    

    FOREIGN KEY (pitch_id) REFERENCES {org}_pitch_master(id),
    FOREIGN KEY (ground_id) REFERENCES {org}_ground_master(id),
    INDEX (pitch_id),
    INDEX (ground_id)
);

SET FOREIGN_KEY_CHECKS=1;
''')
            
            # sql = 
            # print(sql)
            # try:
            #     cursor.execute(sql)
            #     print("huaaaa")
            # except Exception as e:
            #     print(e)
        elif (t == "machinery"):
            sql = f'''SET FOREIGN_KEY_CHECKS=0;
        CREATE TABLE IF NOT EXISTS {tableName} (    
      `id` int NOT NULL AUTO_INCREMENT,
      `equipment_name` varchar(255) NULL,
      `type` varchar(255) NULL,
      `specification` text NULL,
      `unit` varchar(50) NULL,
      `value` text NULL,
      `model` varchar(45) NULL,
      `print_details` varchar(255) NULL,
      PRIMARY KEY (`id`)
            );SET FOREIGN_KEY_CHECKS=1;'''
            cursor.execute(sql)
        elif (t == "match_scores"):
            sql = f'''SET FOREIGN_KEY_CHECKS=0;
            CREATE TABLE IF NOT EXISTS {tableName} (    
            id INT PRIMARY KEY AUTO_INCREMENT,
            match_id INT,
            `day` INT DEFAULT 1,
            team TEXT,
            inning INT,
            `session` INT,
            wickets INT,
            overs FLOAT,
            runs INT,
            winner INT,
            day_end VARCHAR(45),
            FOREIGN KEY (match_id) REFERENCES {org}_match_master(id) ON DELETE CASCADE
        );SET FOREIGN_KEY_CHECKS=1;
                            '''
            cursor.execute(sql)
        elif (t == "match"):
            sql = f'''SET FOREIGN_KEY_CHECKS=0;
          CREATE TABLE IF NOT EXISTS {tableName} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            match_type VARCHAR(255) , 
            name_tournament VARCHAR(255) ,
            team1 VARCHAR(255) ,
            team2 VARCHAR(255) ,
            preparation_date text,
            match_date text,
            from_date text,
            to_date text,
            days_count text,
            start_time text ,
            pitch_id int ,
            ground_id int ,
            is_pitch_level text,
            lawn_height text,
            grass_cover VARCHAR(255),
            min_temp text,
            max_temp text,
            forecast TEXT,
            moisture_upto text,
           
            dew_factor text,
            access_bounce text,
            machinery_id text,
            no_of_passes text ,
            rolling_speed text ,
            last_watering_on text,
            quantity_of_water text ,
            time_of_application text ,
            time_roller text,
            is_daily_watering text ,
        
            mover_machinery_id text,
            date_mowing_done_last text,
            time_of_application_mover text ,
            mowing_done_at_mm text ,
        
            is_fertilizers_used text ,
            fertilizers_details VARCHAR(255),
            chemical_details_remark LONGTEXT,
            remark_by_groundsman VARCHAR(255),
        
            out_machinery_id text,
            out_no_of_passes text,
            out_rolling_speed text,
            out_last_watering_on text,
            out_quantity_of_water text,
            out_time_of_application text,
            out_time_roller text,
            out_is_daily_watering text,
        
            out_mover_machinery_id text,
            out_date_mowing_done_last text,
            time_of_application_out_mover text,
            out_mowing_done_at_mm text,
            out_is_fertilizers_used text,
            out_fertilizers_details VARCHAR(255),
            out_chemical_details_remark LONGTEXT,
            out_remark_by_groundsman VARCHAR(255),
        
            brief_match_pitch_assessment TEXT,
            time_of_application_chemical VARCHAR(255),
            out_time_of_application_chemical VARCHAR(255),
            FOREIGN KEY (pitch_id) REFERENCES {org}_pitch_master(id),
            FOREIGN KEY (ground_id) REFERENCES {org}_ground_master(id),
           
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );
        SET FOREIGN_KEY_CHECKS=1;
        
                            '''
            cursor.execute(sql)
            addMachinery(org)
    except Exception as e:
         print(e.message)

def addMachinery(org):
    try:
        with connection.cursor() as cursor:
            # Define the table name safely
            table_name = f"{org}_machinery_master"
            
            # Updated INSERT query to include "print_details"
            sql = f"""
                INSERT INTO `{table_name}` (`id`, `equipment_name`, `type`, `specification`, `unit`, `value`, `model`, `print_details`)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Updated data with 8 values per record
            data = [
                (1, 'Roller', 'manual', 'Weight', 'kg', '500.00', 'local', 'Manual 500 kg'),
                (2, 'Roller', 'manual', 'Weight', 'kg', '750.00', 'local', 'Manual 750 kg'),
                (3, 'Roller', 'manual', 'Weight', 'kg', '1000.00', 'local', 'Manual 1000 kg'),
                (4, 'Roller', 'manual', 'Weight', 'kg', '1500.00', 'local', 'Manual 1500 kg'),
                (5, 'Roller', 'Mechanised', 'Weight', 'kg', '500.00', 'single drum perol', 'Mechanised 500 kg'),
                (6, 'Roller', 'Mechanised', 'Weight', 'kg', '1000.00', 'single drum perol', 'Mechanised 1000 kg'),
                (7, 'Roller', 'Mechanised', 'Weight', 'kg', '1000.00', 'tandom', 'Mechanised 1000 kg'),
                (8, 'Roller', 'Mechanised', 'Weight', 'kg', '2000.00', 'tandom', 'Mechanised 2000 kg'),
                (9, 'Roller', 'Mechanised', 'Weight', 'kg', '2200.00', 'tandom', 'Mechanised 2200 kg'),
                (10, 'SuperSopper', 'Mechanised', 'length', 'inches', '72.00', 'aqua', 'Mechanised 72 inches'),
                (11, 'SuperSopper', 'Mechanised', 'length', 'inches', '36.00', 'aqua', 'Mechanised 36 inches'),
                (12, 'Aerator Procore 648', 'Mini', 'liquid', 'liter', '0.00', 'petrol', 'Mini Petrol'),
                (13, 'Scarifier Garden', 'Mini', 'liquid', 'liter', '0.00', 'petrol', 'Mini Petrol'),
                (14, 'Lawn Mower Outfield', 'Tractor', 'liquid', 'liter', '0.00', 'petrol black', 'Tractor Petrol black'),
                (15, 'Lawn Mower Outfield', 'Tractor', 'liquid', 'liter', '0.00', 'petrol yellow', 'Tractor Petrol yellow'),
                (16, 'Lawn Mower Outfield', 'Toro', 'liquid', 'liter', '0.00', 'toro 3250', 'Toro 3250'),
                (17, 'Lawn Mower Pitch', 'Mechanised', 'NA', 'NA', '0.00', 'toro 1000', 'Mechanised Toro 1000'),
                (18, 'Top Dresser', 'Mechanised', 'NA', 'NA', '0.00', 'toro', 'Mechanised Toro'),
                (19, 'Kiss Cutter', 'Mechanised', 'NA', 'NA', '0.00', 'turfco', 'Mechanised Turfco'),
                (20, 'Bush Cutter', 'Mechanised', 'NA', 'NA', '0.00', 'styhl', 'Mechanised Styhl'),
                (21, 'Air Compressor', 'Bush Cutter', 'NA', 'NA', '0.00', 'local', 'Bush Cutter'),
                (22, 'Spray Pump', '15 liter', 'liquid', 'liter', '15.00', 'local', '15 liter'),
                (23, 'Spreader', '2', 'NA', 'NA', '2.00', 'local', '2'),
                (24, 'Back lapping Machine', '1', 'NA', 'NA', '1.00', 'local', '1'),
                (25, 'Trolley', 'Trolley', 'NA', 'NA', '0.00', 'local', 'Trolley'),
                (26, 'Pitch Covers', '120x100', 'NA', 'NA', '120x100', 'local', '120x100'),
                (27, 'Pitch Covers', '110x100', 'NA', 'NA', '110x100', 'local', '110x100'),
                (28, 'Pitch Covers', '100x100', 'NA', 'NA', '100x100', 'local', '100x100'),
                (29, 'Pitch Covers', '80x100', 'NA', 'NA', '80x100', 'local', '80x100'),
                (30, 'Pitch Covers', '70x100', 'NA', 'NA', '70x100', 'local', '70x100'),
                (31, 'Pitch Covers', '40x100', 'NA', 'NA', '40x100', 'local', '40x100'),
                (32, 'Pitch Covers', '30x100', 'NA', 'NA', '30x100', 'local', '30x100'),
                (33, 'Pitch Covers', '20x100', 'NA', 'NA', '20x100', 'local', '20x100'),
            ]
            
            # Execute the batch insert
            cursor.executemany(sql, data)
            connection.commit()
            print("Data inserted successfully.")
    except Exception as e:
            print(f"An error occurred: {e}")

def createAllMastersName(instance):
    tables = ["machinery","state","city", "ground", "pitch","match","match_scores","curator_daily_recording"]
    for t in tables:
        tableName=instance.org_id+"_"+t+"_master"
        masterList=MastersList()
        masterList.org_id=instance.org_id
        masterList.tablename=tableName
        masterList.admin_id=instance
        masterList.auth_scorer=True
        masterList.auth_curator=True
        masterList.auth_groundman=True
        masterList.save()

        createTable(tableName,t,instance.org_id)




def create_admin_user(request):
    try:
        if request.method == 'POST':
            form = AdminUserForm(request.POST, request.FILES)
            if form.is_valid():

                instance=form.save()
                print(request, 'Admin user created successfully')
                createAllMastersName(instance)

                return redirect('admin_users_list')  # Redirect to a view that lists admin users
            else:
                print(request, 'Please correct the errors below')
        else:
            form = AdminUserForm()
        return render(request, 'super_admin_user/admin/create_admin.html', {'form': form})
    except Exception as e:
        print(e)
#
# def create_admin_role(request):
#     if request.method == 'POST':
#         form = AdminUserRoleForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance=form.save()
#             messages.success(request, 'Admin user created successfully')
#             # createAllMastersTables(instance)
#             return redirect('admin_users_list')  # Redirect to a view that lists admin users
#         else:
#             messages.error(request, 'Please correct the errors below')
#     else:
#         form = AdminUserForm()
#     return render(request, 'super_admin_user/admin/create_admin.html', {'form': form})

def admin_users_list(request):
    admin_users = AdminUserList.objects.all()
    return render(request, 'super_admin_user/admin/admin_users_list.html', {'admin_users': admin_users})

def admin_user_details(request, admin_id):
    admin = AdminUserList.objects.get(id=admin_id)
    return render(request, 'super_admin_user/admin/admin_user_details.html', {'admin': admin})