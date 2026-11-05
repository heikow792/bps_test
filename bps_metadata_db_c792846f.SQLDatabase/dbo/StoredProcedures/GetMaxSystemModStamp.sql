
        CREATE PROCEDURE [dbo].[GetMaxSystemModStamp]
            @SystemName NVARCHAR(50),
            @ObjectName NVARCHAR(255)
        AS
        BEGIN
            SET NOCOUNT ON;

            IF EXISTS (SELECT 1 FROM [dbo].[SalesforceTableCheckpoint] WHERE SystemName = @SystemName AND ObjectName = @ObjectName) 
            BEGIN
                SELECT FORMAT(MaxSystemModStamp, 'yyyy-MM-ddThh:mm:ssZ'), MaxSystemModStamp
                FROM [dbo].[SalesforceTableCheckpoint]
                WHERE SystemName = @SystemName AND ObjectName = @ObjectName
            END ELSE BEGIN
                SELECT NULL AS MaxSystemModStamp;
            END
        END

GO

