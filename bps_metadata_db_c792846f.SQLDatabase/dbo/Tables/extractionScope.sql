CREATE TABLE [dbo].[extractionScope] (
    [SystemName]  NVARCHAR (50)  NOT NULL,
    [DatasetName] NVARCHAR (300) NOT NULL,
    [TableName]   NVARCHAR (300) NOT NULL,
    [IsEnabled]   BIT            CONSTRAINT [DF_extractionScope_IsEnabled] DEFAULT ((1)) NOT NULL,
    CONSTRAINT [PK_extractionScope] PRIMARY KEY CLUSTERED ([SystemName] ASC, [DatasetName] ASC, [TableName] ASC)
);


GO

