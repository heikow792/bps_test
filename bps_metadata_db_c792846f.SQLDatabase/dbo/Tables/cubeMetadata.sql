CREATE TABLE [dbo].[cubeMetadata] (
    [SystemName]       NVARCHAR (50)   NOT NULL,
    [RelationshipName] NVARCHAR (300)  NOT NULL,
    [FactTable]        NVARCHAR (300)  NOT NULL,
    [DimensionTable]   NVARCHAR (300)  NOT NULL,
    [JoinCondition]    NVARCHAR (1000) NOT NULL,
    [SKColumn]         NVARCHAR (300)  NOT NULL,
    [DimColumns]       NVARCHAR (1000) NOT NULL,
    [JoinOrder]        INT             NOT NULL,
    CONSTRAINT [PK_cubeMetadata] PRIMARY KEY CLUSTERED ([SystemName] ASC, [RelationshipName] ASC)
);


GO

