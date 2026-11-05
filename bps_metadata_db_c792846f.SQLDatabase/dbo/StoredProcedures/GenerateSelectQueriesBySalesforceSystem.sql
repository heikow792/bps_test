
        CREATE PROCEDURE [dbo].[GenerateSelectQueriesBySalesforceSystem]
            @SystemName NVARCHAR(50),
            @ObjectNames NVARCHAR(MAX) = NULL -- Optional comma-separated list of object names
        AS
        BEGIN
            SET NOCOUNT ON;

            -- Create a temporary table to hold the parsed object names
            DECLARE @FilteredObjectNames TABLE (ObjectName NVARCHAR(100));

            -- Parse the comma-separated list if provided
            IF @ObjectNames IS NOT NULL AND LEN(@ObjectNames) > 0
            BEGIN
                INSERT INTO @FilteredObjectNames
                SELECT TRIM(value) FROM STRING_SPLIT(@ObjectNames, ',');
            END

            SELECT
                main.CDSViewName AS ObjectName,
                'SELECT ' +
                STUFF((
                    SELECT ', ' + fieldName
                    FROM [dbo].[FieldMetadata] AS sub
                    WHERE sub.CDSViewName = main.CDSViewName
                    AND sub.SystemName = @SystemName
                    FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'),
                    1, 2, '') + 
                ' FROM ' + main.CDSViewName AS select_query
            FROM [dbo].[FieldMetadata] AS main
            WHERE main.SystemName = @SystemName
              AND (@ObjectNames IS NULL OR main.CDSViewName IN (SELECT ObjectName FROM @FilteredObjectNames))
              AND main.CDSViewName IN (
                  SELECT TableName
                  FROM dbo.ExtractionScope es
                  JOIN dbo.systemDetails sd 
                  on es.SystemName = sd.SystemName
                  WHERE isEnabled = 1 
                    AND sd.SourceType = 'Salesforce'
                    AND es.SystemName = @SystemName
              )
            GROUP BY main.CDSViewName;
        END;

GO

