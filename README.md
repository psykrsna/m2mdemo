# m2mdemo
Creating a sample django project to demonstrate a Many To Many relationship.


**Entities**

1. Software
2. Programmer

**Relationship**

The relationship between these two entities is many to many, as one software can be written by many programmers and conversely one programmer can write more than one software.

**DB Tables**

* demo_software
* demo_programmer
* demo_software_programmers

**DB Table Attributes**

demo_software

    * id (primary key)
    * name (varchar)
    * version (varchar)

demo_programmer

    * username (primary key)

demo_software_programmers

    * id (primary key)
    * software_id (foreign key)
    * programmer_id (foreign key)


The relationship between demo_software & demo_software_programmers is One to Many. Between demo_software_programmers & demo_programmer is Many to One.

Hence effectively creating a Many to Many relationship between Software and Programmer data models.

**The SQL implementation**


    BEGIN;
    CREATE TABLE "demo_programmer" ("username" varchar(30) NOT NULL PRIMARY KEY);
    CREATE TABLE "demo_software" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(60) NOT NULL, "version" varchar(10) NOT NULL);
    CREATE TABLE "demo_software_programmers" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "software_id" integer NOT NULL REFERENCES "demo_software" ("id"), "programmer_id" varchar(30) NOT NULL REFERENCES "demo_programmer" ("username"), UNIQUE ("software_id", "programmer_id"));
    CREATE INDEX "demo_software_programmers_01e7c7a4" ON "demo_software_programmers" ("software_id");
    CREATE INDEX "demo_software_programmers_1588157f" ON "demo_software_programmers" ("programmer_id");

    COMMIT;

