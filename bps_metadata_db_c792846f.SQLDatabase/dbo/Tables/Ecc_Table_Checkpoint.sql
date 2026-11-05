CREATE TABLE [dbo].[Ecc_Table_Checkpoint] (
    [TableName]             NVARCHAR (200) NOT NULL,
    [SystemName]            NVARCHAR (10)  NOT NULL,
    [RelatedCDSViewName]    NVARCHAR (200) NOT NULL,
    [MaxProcessedTimestamp] DATETIME2 (7)  NULL,
    PRIMARY KEY CLUSTERED ([TableName] ASC, [SystemName] ASC, [RelatedCDSViewName] ASC)
);


GO

