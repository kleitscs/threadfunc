from main import cursor
import fractions

def mixed_to_float(dia):
    return float(sum(fractions.Fraction(term) for term in dia.split()))


def name(part):
    # type: (object) -> object
    """

    :rtype: object
    """
    cursor.execute('''SELECT c.[Name]
                        FROM [LocknutData].[dbo].[PartNumber] a

                        INNER JOIN [LocknutData].[dbo].[Pitch2ThreadDiameter] b
                        on b.Pitch2ThreadDiameterID = a.Pitch2ThreadDiameterID

                        INNER JOIN [LocknutData].[dbo].[ThreadDiameter] c
                        on c.ThreadDiameterID = b.ThreadDiameterID

                        WHERE a.Name = '{}';'''.format(part))
    return cursor.fetchone()[0]
    cursor.close()


def unique(part):
    cursor.execute('''SELECT b.ThreadDiameterID
                        FROM [LocknutData].[dbo].[PartNumber] a

                        INNER JOIN [LocknutData].[dbo].[Pitch2ThreadDiameter] b
                        on b.Pitch2ThreadDiameterID = a.Pitch2ThreadDiameterID

                        WHERE a.Name = '{}';'''.format(part))
    return cursor.fetchone()[0]
    cursor.close()


def pitch(sqlid):
    cursor.execute('''SELECT c.Name
                        FROM [LocknutData].[dbo].[Pitch2ThreadDiameter] a

                        INNER JOIN [LocknutData].[dbo].[Pitch] b
                        on b.PitchID = c.PitchID

                        WHERE a.ThreadDiameterID = '{}';'''.format(sqlid))
    return cursor.fetchall()
    cursor.close()


def getid(dia):
    cursor.execute('''SELECT ThreadDiameterID 
           FROM LocknutData.dbo.ThreadDiameter 
           WHERE Name = '{}';'''
                   .format(dia))
    if cursor.rowcount == 0:
        if dia[:1] == 'M':
            unit = 5
            eqv = float(dia[1:]) * 0.0393701
        else:
            unit = 4
            eqv = mixed_to_float(dia)

        cursor.execute('''INSERT INTO LocknutData.dbo.ThreadDiameter
                               (Name, MeasurementUnitID, InchMeasurementEquivalent)
                               VALUES ('{}', {}, {});'''.format(dia, unit, eqv))
    cursor.execute('''SELECT ThreadDiameterID 
                           FROM LocknutData.dbo.ThreadDiameter 
                           WHERE Name = '{}';'''.format(dia))
    return cursor.fetchone()[0]
    cursor.close()


def units(dia):
    cursor.execute('''SELECT MeasurementUnitID
           FROM LocknutData.dbo.ThreadDiameter 
           WHERE Name = '{}';'''
                   .format(dia))
    return cursor.fetchone()[0]
    cursor.close()
