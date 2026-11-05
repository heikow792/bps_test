CREATE TABLE [dbo].[viewMetadata] (
    [SystemName]         NVARCHAR (50)  NOT NULL,
    [CDSViewName]        NVARCHAR (300) NOT NULL,
    [Context]            NVARCHAR (300) NOT NULL,
    [Description]        NVARCHAR (300) NULL,
    [Type]               NVARCHAR (300) NOT NULL,
    [ODPName]            NVARCHAR (300) NOT NULL,
    [Delta]              BIT            NOT NULL,
    [KeyFields]          NVARCHAR (MAX) NOT NULL,
    [relatedCDSViewName] NVARCHAR (300) NULL,
    CONSTRAINT [PK_viewMetadata] PRIMARY KEY CLUSTERED ([SystemName] ASC, [CDSViewName] ASC)
);


GO

