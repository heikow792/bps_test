
        CREATE   PROCEDURE [dbo].[InsertExtractionLogs]
            @TimeStamp DATETIME2,
            @PipelineName VARCHAR(400),
            @ExecutionId VARCHAR(400),
            @Status VARCHAR(400),
            @CDSView VARCHAR(300),
            @SystemName VARCHAR(50),
            @ConnectorType VARCHAR(400),
            @ODPName VARCHAR(400)
        AS
        BEGIN
            INSERT INTO [dbo].[ExtractionLogs]
            VALUES (@TimeStamp, @PipelineName, @ExecutionId, @Status, @CDSView, @SystemName, @ConnectorType, @ODPName)
        END

GO

