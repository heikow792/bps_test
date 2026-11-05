CREATE TABLE [dbo].[OrchestrationLogs] (
    [TimeStamp]     DATETIME       NOT NULL,
    [PipelineName]  NVARCHAR (100) NOT NULL,
    [ExecutionId]   NVARCHAR (100) NOT NULL,
    [Status]        NVARCHAR (100) NOT NULL,
    [VersionNumber] NVARCHAR (100) NOT NULL
);


GO

