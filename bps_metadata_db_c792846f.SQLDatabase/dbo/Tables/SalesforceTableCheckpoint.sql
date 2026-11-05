CREATE TABLE [dbo].[SalesforceTableCheckpoint] (
    [SystemName]        NVARCHAR (50)  NOT NULL,
    [ObjectName]        NVARCHAR (300) NOT NULL,
    [MaxSystemModStamp] DATETIME2 (7)  NULL
);


GO

