from main import cursor


def addnew(standard_i_d, pitch2_thread_diameter_i_d, pitch_thread_diameter_designation_i_d):
    query = '''INSERT INTO [LocknutData].[dbo].[Standard2PitchThreadDiameter] 
                ([StandardID]
                ,[Pitch2ThreadDiameterID]
                ,[PitchThreadDiameterDesignationID])
                SELECT {:d}
                        ,{:d}
                        ,{:d}
                WHERE NOT EXISTS (SELECT 1 
                                    FROM [LocknutData].[dbo].[Standard2PitchThreadDiameter]  
                                    WHERE [StandardID] = {:d}
                                    AND [Pitch2ThreadDiameterID] = {:d}
                                    AND [PitchThreadDiameterDesignationID] = {:d});''' \
        .format(standard_i_d, pitch2_thread_diameter_i_d, pitch_thread_diameter_designation_i_d, standard_i_d,
                pitch2_thread_diameter_i_d, pitch_thread_diameter_designation_i_d)

    cursor.execute(query)
    cursor.commit()


def threaddes(part_number):
    query = '''SELECT a.[Name]
                            ,d.[Name]

                        	FROM [LocknutData].[dbo].[ThreadDiameter] a

                        	INNER JOIN [LocknutData].[dbo].[MeasurementUnit] b
                        		on b.MeasurementUnitID = a.MeasurementUnitID

                        	INNER JOIN [LocknutData].[dbo].[Pitch2ThreadDiameter] c
                        		on c.ThreadDiameterID = a.ThreadDiameterID

                        	INNER JOIN [LocknutData].[dbo].[Pitch] d
                        		on d.PitchID = c.PitchID

                        	INNER JOIN [LocknutData].[dbo].[PartNumber] e
                        		on e.Pitch2ThreadDiameterID = c.Pitch2ThreadDiameterID

                        	Where e.Name = '{}';''' \
        .format(part_number)

    result = cursor.fetchall()

    for item in result:
        threaddesc = item[0] + ' x ' + item[1]

    return threaddesc
    #
    # Stop using the query
    cursor.close()
