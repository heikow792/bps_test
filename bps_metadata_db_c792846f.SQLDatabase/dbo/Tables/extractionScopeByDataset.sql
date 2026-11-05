CREATE TABLE [dbo].[extractionScopeByDataset] (
    [SystemName]  NVARCHAR (50)  NOT NULL,
    [DatasetName] NVARCHAR (300) NOT NULL,
    [IsEnabled]   BIT            CONSTRAINT [DF_extractionScopeByDataset_IsEnabled] DEFAULT ((1)) NOT NULL,
    CONSTRAINT [PK_extractionScopeByDataset] PRIMARY KEY CLUSTERED ([SystemName] ASC, [DatasetName] ASC)
);


GO

