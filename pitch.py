from main import cursor


def name(part):
    cursor.execute('''SELECT c.[Name]
                        FROM [LocknutData].[dbo].[PartNumber] a

                        INNER JOIN [LocknutData].[dbo].[Pitch2ThreadDiameter] b
                        on b.Pitch2ThreadDiameterID = a.Pitch2ThreadDiameterID

                        INNER JOIN [LocknutData].[dbo].[Pitch] c
                        on c.PitchID = b.PitchID

                        WHERE a.Name = '{}';'''.format(part))
    return cursor.fetchone()[0]
    cursor.close()


def unique(part):
    cursor.execute('''SELECT b.PitchID
                        FROM [LocknutData].[dbo].[PartNumber] a

                        INNER JOIN [LocknutData].[dbo].[Pitch2ThreadDiameter] b
                        on b.Pitch2ThreadDiameterID = a.Pitch2ThreadDiameterID

                        WHERE a.Name = '{}';'''.format(part))
    return cursor.fetchone()[0]
    cursor.close()


def diameterid(sqlid):
    cursor.execute('''SELECT b.ThreadDiameterID
                        FROM [LocknutData].[dbo].[Pitch2ThreadDiameter] a

                        INNER JOIN [LocknutData].[dbo].[ThreadDiameter] b
                        on b.ThreadDiameterID = a.Pitch2ThreadDiameterID

                        WHERE a.PitchID = {:d};'''.format(sqlid))
    return cursor.fetchall()
    cursor.close()


def getid(pitch):
    sql = '''INSERT INTO LocknutData.dbo.Pitch ([Name])
                SELECT %s
                WHERE NOT EXISTS (SELECT 1
                                    FROM LocknutData.dbo.Pitch
                                    WHERE [Name] = '%s');''' % (pitch, pitch)
    cursor.execute(sql)
    cursor.execute('''SELECT PitchID 
                       FROM LocknutData.dbo.Pitch 
                       WHERE Name = '{}';'''.format(pitch))

    return cursor.fetchone()[0]
    cursor.close()

