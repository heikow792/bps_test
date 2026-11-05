CREATE TABLE [dbo].[AdfExtractionCheckpoint] (
    [CDSViewName]            NVARCHAR (300) NOT NULL,
    [systemName]             NVARCHAR (50)  NOT NULL,
    [checkpointId]           NVARCHAR (36)  NULL,
    [maxId]                  BIGINT         NULL,
    [lastProcessedTimestamp] DATETIME2 (7)  NULL,
    [systemType]             NVARCHAR (50)  NULL,
    CONSTRAINT [PK_AdfExtractionCheckpoint] PRIMARY KEY CLUSTERED ([CDSViewName] ASC, [systemName] ASC)
);


GO

