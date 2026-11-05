CREATE TABLE [dbo].[VersionDetails] (
    [VersionNumber]               NVARCHAR (100) NOT NULL,
    [FirstExecutionDate]          DATETIME       NOT NULL,
    [LastExecutionDate]           DATETIME       NOT NULL,
    [LastSuccessfulExecutionDate] DATETIME       NULL
);


GO

