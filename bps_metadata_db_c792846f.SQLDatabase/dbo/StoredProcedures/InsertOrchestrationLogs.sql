
        CREATE   PROCEDURE [dbo].[InsertOrchestrationLogs]
            @TimeStamp DATETIME2,
            @PipelineName VARCHAR(400),
            @ExecutionId VARCHAR(400),
            @Status VARCHAR(400),
            @VersionNumber VARCHAR(400)
        AS
        BEGIN
            INSERT INTO [dbo].[OrchestrationLogs]
            VALUES (@TimeStamp, @PipelineName, @ExecutionId, @Status, @VersionNumber)
        END

GO

