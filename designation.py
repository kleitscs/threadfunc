from main import cursor
from threadfunk import diameter
from threadfunk import pitch


def relateid(diametername, pitchname):
    """
    :type diametername: object
    :type pitchname: object
    """
    tid = diameter.getid(diametername)
    pid = pitch.getid(pitchname)

    cursor.execute('''SELECT Pitch2ThreadDiameterID
                       FROM LocknutData.dbo.Pitch2ThreadDiameter
                       WHERE PitchID = %i
                       AND ThreadDiameterID = %i''' % (pid, tid))
    if cursor.rowcount == 0:
        cursor.execute('''INSERT INTO LocknutData.dbo.Pitch2ThreadDiameter
                           (PitchID, ThreadDiameterID)
                           VALUES (%i, %i);'''
                       % (pid, tid))
        cursor.commit()
    cursor.execute('''SELECT Pitch2ThreadDiameterID
                       FROM LocknutData.dbo.Pitch2ThreadDiameter
                       WHERE PitchID = %i
                       AND ThreadDiameterID = %i''' % (pid, tid))
    return cursor.fetchone()[0]


def getid(designation):
    cursor.execute('''SELECT PitchThreadDiameterDesignationID 
           FROM LocknutData.dbo.PitchThreadDiameterDesignation
           WHERE Name = '{}';'''
                   .format(designation))
    if cursor.rowcount == 0:
        cursor.execute('''INSERT INTO LocknutData.dbo.PitchThreadDiameterDesignation
                           (Name)
                           VALUES ('{}');'''
                       .format(designation))
        cursor.commit()
    cursor.execute('''SELECT PitchThreadDiameterDesignationID 
           FROM LocknutData.dbo.PitchThreadDiameterDesignation
           WHERE Name = '{}';'''
                   .format(designation))
    return cursor.fetchone()[0]
    cursor.close()


#def name(part):
