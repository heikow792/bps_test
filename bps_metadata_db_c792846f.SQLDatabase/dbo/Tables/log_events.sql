CREATE TABLE [dbo].[log_events] (
    [ServiceActivityId]    NVARCHAR (400) NULL,
    [level]                NVARCHAR (100) NULL,
    [PreciseTimestamp]     NVARCHAR (100) NULL,
    [SystemName]           NVARCHAR (400) NULL,
    [TableName]            NVARCHAR (400) NULL,
    [Message]              NVARCHAR (MAX) NULL,
    [Stage]                NVARCHAR (100) NULL,
    [LogType]              NVARCHAR (100) NULL,
    [rootNotebookName]     NVARCHAR (400) NULL,
    [currentNotebookName]  NVARCHAR (400) NULL,
    [currentNotebookId]    NVARCHAR (400) NULL,
    [currentWorkspaceName] NVARCHAR (400) NULL,
    [currentWorkspaceId]   NVARCHAR (400) NULL,
    [defaultLakehouseName] NVARCHAR (400) NULL,
    [environmentId]        NVARCHAR (400) NULL,
    [isForPipeline]        NVARCHAR (50)  NULL,
    [isForInteractive]     NVARCHAR (50)  NULL,
    [isReferenceRun]       NVARCHAR (50)  NULL
);


GO

