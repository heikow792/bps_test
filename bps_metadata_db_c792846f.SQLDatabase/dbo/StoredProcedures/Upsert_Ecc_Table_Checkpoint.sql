
    CREATE PROCEDURE [dbo].[Upsert_Ecc_Table_Checkpoint]
        @TableName NVARCHAR(200),
        @SystemName NVARCHAR(10),
        @RelatedCDSViewName NVARCHAR(200) = NULL,
        @MaxProcessedTimestamp DATETIME2(7) = NULL
    AS
    BEGIN
        SET NOCOUNT ON;

        MERGE [dbo].[Ecc_Table_Checkpoint] AS target
        USING (
            SELECT @TableName AS TableName,
                   @SystemName AS SystemName,
                   @RelatedCDSViewName AS RelatedCDSViewName,
                   @MaxProcessedTimestamp AS MaxProcessedTimestamp
        ) AS source
        ON (target.TableName = source.TableName
            AND target.SystemName = source.SystemName
            AND (
                (target.RelatedCDSViewName = source.RelatedCDSViewName) OR
                (target.RelatedCDSViewName IS NULL AND source.RelatedCDSViewName IS NULL)
            ))
        WHEN MATCHED THEN
            UPDATE SET MaxProcessedTimestamp = source.MaxProcessedTimestamp
        WHEN NOT MATCHED THEN
            INSERT (TableName, SystemName, RelatedCDSViewName, MaxProcessedTimestamp)
            VALUES (source.TableName, source.SystemName, source.RelatedCDSViewName, source.MaxProcessedTimestamp);
    END

GO

