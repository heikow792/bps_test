
    CREATE   PROCEDURE [dbo].[GetCheckpointId]
        @CDSViewName nvarchar(300),
        @SystemName nvarchar(50)
    AS
    BEGIN
        SET NOCOUNT ON;
        DECLARE @CheckpointId nvarchar(36)
        
        -- Check if record exists
        SELECT @CheckpointId = checkpointId 
        FROM dbo.AdfExtractionCheckpoint 
        WHERE CDSViewName = @CDSViewName AND systemName = @SystemName;

        -- If record doesn't exist or checkpoint is null, create/update it
        IF @CheckpointId IS NULL
        BEGIN
            -- Generate new GUID
            SET @CheckpointId = CONVERT(nvarchar(36), NEWID());
            
            -- Use MERGE to handle both insert and update scenarios
            MERGE dbo.AdfExtractionCheckpoint AS target
            USING (SELECT @CDSViewName as CDSViewName, @SystemName as systemName, @CheckpointId as checkpointId) AS source
            ON (target.CDSViewName = source.CDSViewName AND target.systemName = source.systemName)
            WHEN MATCHED THEN
                UPDATE SET checkpointId = source.checkpointId
            WHEN NOT MATCHED THEN
                INSERT (CDSViewName, systemName, checkpointId)
                VALUES (source.CDSViewName, source.systemName, source.checkpointId);
        END
        
        SELECT @CheckpointId as CheckpointId;
    END

GO

