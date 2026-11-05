CREATE TABLE [dbo].[fieldMetadata] (
    [systemName]   NVARCHAR (50)  NOT NULL,
    [CDSViewName]  NVARCHAR (300) NOT NULL,
    [fieldName]    NVARCHAR (200) NOT NULL,
    [dataType]     NVARCHAR (50)  NULL,
    [length]       INT            NULL,
    [decimals]     INT            NULL,
    [systemType]   NVARCHAR (50)  NULL,
    [Precision]    INT            NULL,
    [Scale]        INT            NULL,
    [IsCalculated] BIT            NULL,
    CONSTRAINT [PK_fieldMetadata] PRIMARY KEY CLUSTERED ([systemName] ASC, [CDSViewName] ASC, [fieldName] ASC)
);


GO

