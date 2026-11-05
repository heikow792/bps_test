CREATE TABLE [dbo].[systemDetails] (
    [SystemName]     NVARCHAR (50)  NOT NULL,
    [SourceType]     NVARCHAR (50)  NOT NULL,
    [SystemType]     NVARCHAR (50)  NOT NULL,
    [SystemNumber]   NVARCHAR (50)  NOT NULL,
    [SystemVersion]  NVARCHAR (100) NOT NULL,
    [ConnectionType] NVARCHAR (100) NOT NULL,
    [ServerName]     NVARCHAR (MAX) NOT NULL,
    [ClientId]       NVARCHAR (50)  NOT NULL,
    [UserName]       NVARCHAR (50)  NOT NULL,
    [SecretName]     NVARCHAR (50)  NOT NULL,
    [SubscriberName] NVARCHAR (50)  NOT NULL,
    CONSTRAINT [PK_systemDetails] PRIMARY KEY CLUSTERED ([SystemName] ASC, [ConnectionType] ASC)
);


GO

