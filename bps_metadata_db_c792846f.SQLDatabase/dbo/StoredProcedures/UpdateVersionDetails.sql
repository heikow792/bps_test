
        CREATE PROCEDURE [dbo].[UpdateVersionDetails]
            @VersionNumber nvarchar(100),
            @IsExecutionSuccessful bit
        AS
        BEGIN
            SET NOCOUNT ON;

            DECLARE @FirstExecutionDate datetime
            DECLARE @LastExecutionDate datetime
            DECLARE @LastSuccessfulExecutionDate datetime

            SELECT @FirstExecutionDate = FirstExecutionDate, @LastExecutionDate = LastExecutionDate, @LastSuccessfulExecutionDate = LastSuccessfulExecutionDate
            FROM [dbo].[VersionDetails]
            WHERE VersionNumber = @VersionNumber

            IF @FirstExecutionDate IS NULL
            BEGIN
                INSERT INTO [dbo].[VersionDetails] (VersionNumber, FirstExecutionDate, LastExecutionDate, LastSuccessfulExecutionDate)
                VALUES (@VersionNumber, GETDATE(), GETDATE(), NULL)
            END
            ELSE
            BEGIN
                UPDATE [dbo].[VersionDetails]
                SET LastExecutionDate = GETDATE()
                WHERE VersionNumber = @VersionNumber

                IF @IsExecutionSuccessful = 1
                BEGIN
                    UPDATE [dbo].[VersionDetails]
                    SET LastSuccessfulExecutionDate = GETDATE()
                    WHERE VersionNumber = @VersionNumber
                END
            END
        END

GO

