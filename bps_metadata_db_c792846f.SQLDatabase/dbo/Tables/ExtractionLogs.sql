CREATE TABLE [dbo].[ExtractionLogs] (
    [TimeStamp]     DATETIME2 (7) NULL,
    [PipelineName]  VARCHAR (400) NULL,
    [ExecutionId]   VARCHAR (400) NULL,
    [Status]        VARCHAR (400) NULL,
    [CDSView]       VARCHAR (300) NULL,
    [SystemName]    VARCHAR (50)  NULL,
    [ConnectorType] VARCHAR (400) NULL,
    [ODPName]       VARCHAR (400) NULL
);


GO

